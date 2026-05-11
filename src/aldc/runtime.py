"""Runtime: model-call abstraction with two backends.

Backends:
    - ``claude_code`` (default): routes through ``claude -p`` subprocess,
      using the user's Claude Code / Max subscription. Free of per-call charges.
    - ``api``: routes through the official Anthropic API. Per-call billing,
      used for the paper's reproducibility appendix and the live-provider arm.

Selected via env var ``ALDC_BACKEND`` (case-insensitive). Both backends accept
the same arguments and return the same shape, so consumers (corpus_gen,
detector, baselines) are backend-agnostic.

This file is the *Wirtschaftliche Zumutbarkeit* (economic feasibility) test of
the Performable Duty doctrine, made executable. Either backend reaches the same
output shape; the legal argument doesn't depend on which one.
"""

from __future__ import annotations

import asyncio
import json
import logging
import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

from tenacity import (
    AsyncRetrying,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

logger = logging.getLogger(__name__)

BackendName = Literal["claude_code", "api"]


def _resolve_backend() -> BackendName:
    raw = os.environ.get("ALDC_BACKEND", "claude_code").strip().lower()
    if raw not in ("claude_code", "api"):
        raise ValueError(
            f"ALDC_BACKEND={raw!r} invalid. Use 'claude_code' (Max subscription, default) "
            f"or 'api' (paid Anthropic API)."
        )
    return raw  # type: ignore[return-value]


@dataclass(frozen=True)
class ModelCallResult:
    """A normalised result from either backend.

    ``structured_output`` is the parsed JSON object that conforms to the
    requested ``json_schema``. ``text`` is the free-form text response
    (used by baselines.py for continuations; empty for structured calls).
    ``model_version`` is a stable identifier suitable for the paper appendix.
    ``cost_usd_equivalent`` is the API-equivalent cost in USD: 0.0 if the call
    actually ran on Max, the metered cost if on API.
    """

    structured_output: dict[str, Any] | None
    text: str
    model_version: str
    backend: BackendName
    latency_ms: int
    cost_usd_equivalent: float
    raw_response: dict[str, Any] | None = None


class TransientCallError(RuntimeError):
    """Retryable error from a backend (rate limit, timeout, transient API failure)."""


class FatalCallError(RuntimeError):
    """Non-retryable error (schema violation after final retry, auth failure)."""


# ---------- Claude Code (subprocess) backend --------------------------------


CLAUDE_BIN = os.environ.get("CLAUDE_BIN", "claude")
DEFAULT_TIMEOUT_SEC = int(os.environ.get("ALDC_CLI_TIMEOUT_SEC", "180"))
# Conservative rate budget for the Max subscription. Override via env if needed.
DEFAULT_CONCURRENCY = int(os.environ.get("ALDC_CONCURRENCY", "4"))

_global_semaphore: asyncio.Semaphore | None = None


def _semaphore() -> asyncio.Semaphore:
    global _global_semaphore
    if _global_semaphore is None:
        _global_semaphore = asyncio.Semaphore(DEFAULT_CONCURRENCY)
    return _global_semaphore


async def _claude_code_call(
    *,
    system_prompt: str,
    user_message: str,
    json_schema: dict | None,
    model: str = "opus",
    timeout_sec: int = DEFAULT_TIMEOUT_SEC,
) -> ModelCallResult:
    """Spawn ``claude -p`` and return a normalised result.

    The Claude Code CLI handles auth via the user's subscription. We pass the
    system prompt via stdin (to avoid command-line length / quoting issues)
    using ``--system-prompt-file=/dev/stdin``-style; but since CLI flags don't
    universally support stdin, we write the system prompt to a temp file in
    /tmp instead. The user-message arg is passed inline.
    """
    import tempfile

    args: list[str] = [
        CLAUDE_BIN,
        "-p",
        "--output-format",
        "json",
        "--model",
        model,
        "--no-session-persistence",
    ]

    # Write the system prompt to a temp file. claude -p supports
    # --append-system-prompt-file <path>.
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False, prefix="aldc-sys-"
    ) as fh:
        fh.write(system_prompt)
        sys_path = fh.name

    args.extend(["--append-system-prompt-file", sys_path])

    if json_schema is not None:
        args.extend(["--json-schema", json.dumps(json_schema, separators=(",", ":"))])

    args.append(user_message)

    started = time.perf_counter()
    try:
        proc = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        try:
            stdout_bytes, stderr_bytes = await asyncio.wait_for(
                proc.communicate(), timeout=timeout_sec
            )
        except asyncio.TimeoutError as exc:
            proc.kill()
            raise TransientCallError(f"claude -p timed out after {timeout_sec}s") from exc
    finally:
        # Best effort cleanup of the temp file.
        try:
            os.unlink(sys_path)
        except OSError:
            pass

    elapsed_ms = int((time.perf_counter() - started) * 1000)

    if proc.returncode != 0:
        err = stderr_bytes.decode("utf-8", errors="replace")
        out = stdout_bytes.decode("utf-8", errors="replace")
        # Rate limit / overload responses are retryable.
        if any(s in err.lower() or s in out.lower() for s in ("rate", "overload", "timeout", "429")):
            raise TransientCallError(f"claude -p transient failure: {err[:500]}")
        raise FatalCallError(
            f"claude -p exited {proc.returncode}: stderr={err[:500]} stdout={out[:500]}"
        )

    try:
        payload = json.loads(stdout_bytes.decode("utf-8"))
    except json.JSONDecodeError as exc:
        raise FatalCallError(f"claude -p stdout was not JSON: {stdout_bytes[:500]!r}") from exc

    if payload.get("is_error"):
        raise TransientCallError(f"claude -p returned is_error=true: {payload}")

    text = payload.get("result", "") or ""
    structured = payload.get("structured_output")
    if json_schema is not None and structured is None:
        # Schema was requested but model didn't conform — retry path.
        raise TransientCallError(
            f"json_schema requested but structured_output missing. "
            f"result_preview={text[:300]!r}"
        )

    # Try to pick the most accurate model identifier from modelUsage. The CLI
    # may use Haiku for orchestration; we want the model that did the actual
    # classification, which is the one whose output_tokens exceed a trivial
    # threshold.
    model_version = model
    usage_block = payload.get("modelUsage", {}) or {}
    best_model = None
    best_output = 0
    for name, stats in usage_block.items():
        out_tokens = stats.get("outputTokens", 0)
        if out_tokens > best_output:
            best_output = out_tokens
            best_model = name
    if best_model:
        model_version = best_model

    cost = float(payload.get("total_cost_usd", 0.0))

    return ModelCallResult(
        structured_output=structured,
        text=text,
        model_version=f"{model_version}@claude_code",
        backend="claude_code",
        latency_ms=elapsed_ms,
        cost_usd_equivalent=cost,
        raw_response=payload,
    )


# ---------- Anthropic API backend ------------------------------------------


_api_client = None


async def _api_call(
    *,
    system_prompt: str,
    user_message: str,
    json_schema: dict | None,
    model: str = "opus",
    timeout_sec: int = DEFAULT_TIMEOUT_SEC,
) -> ModelCallResult:
    """Backend that uses anthropic.AsyncAnthropic + tool_use to enforce schema."""
    global _api_client
    from anthropic import APIError, AsyncAnthropic
    from anthropic.types import TextBlock, ToolUseBlock
    from dotenv import load_dotenv

    load_dotenv()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise FatalCallError(
            "ALDC_BACKEND=api but ANTHROPIC_API_KEY is unset. "
            "Either set the key, or switch to ALDC_BACKEND=claude_code."
        )
    if _api_client is None:
        _api_client = AsyncAnthropic()

    model_full = {
        "opus": "claude-opus-4-7",
        "sonnet": "claude-sonnet-4-6",
        "haiku": "claude-haiku-4-5-20251001",
    }.get(model, model)

    kwargs: dict[str, Any] = {
        "model": model_full,
        "max_tokens": 4096,
        "temperature": 0.7,
        "system": system_prompt,
        "messages": [{"role": "user", "content": user_message}],
    }

    if json_schema is not None:
        kwargs["tools"] = [
            {
                "name": "submit",
                "description": "Submit the structured response in the required JSON schema.",
                "input_schema": json_schema,
            }
        ]
        kwargs["tool_choice"] = {"type": "tool", "name": "submit"}

    started = time.perf_counter()
    try:
        response = await _api_client.messages.create(**kwargs)
    except APIError as exc:
        if exc.status_code in (429, 503, 504):
            raise TransientCallError(str(exc)) from exc
        raise FatalCallError(str(exc)) from exc
    elapsed_ms = int((time.perf_counter() - started) * 1000)

    structured: dict | None = None
    text = ""
    for block in response.content:
        if isinstance(block, ToolUseBlock):
            structured = dict(block.input)  # type: ignore[arg-type]
        elif isinstance(block, TextBlock):
            text = (text + "\n" + block.text).strip() if text else block.text

    if json_schema is not None and structured is None:
        raise TransientCallError(
            f"api backend: submit tool not called. text_preview={text[:300]!r}"
        )

    # Rough cost ledger; precise prices live in detector.py/baselines.py.
    cost = 0.0  # consumer modules already track per-call price; runtime stays neutral

    return ModelCallResult(
        structured_output=structured,
        text=text,
        model_version=f"{response.model}@api",
        backend="api",
        latency_ms=elapsed_ms,
        cost_usd_equivalent=cost,
        raw_response={"usage": response.usage.model_dump() if hasattr(response.usage, "model_dump") else None},
    )


# ---------- Public API -----------------------------------------------------


async def call(
    *,
    system_prompt: str,
    user_message: str,
    json_schema: dict | None = None,
    model: str = "opus",
    timeout_sec: int = DEFAULT_TIMEOUT_SEC,
    max_attempts: int = 3,
) -> ModelCallResult:
    """Backend-agnostic model call with retry and concurrency limiting.

    Selects the backend from ``ALDC_BACKEND`` at call time.
    """
    backend = _resolve_backend()
    impl = _claude_code_call if backend == "claude_code" else _api_call

    async for attempt in AsyncRetrying(
        stop=stop_after_attempt(max_attempts),
        wait=wait_exponential(multiplier=1, min=3, max=30),
        retry=retry_if_exception_type(TransientCallError),
        reraise=True,
    ):
        with attempt:
            async with _semaphore():
                return await impl(
                    system_prompt=system_prompt,
                    user_message=user_message,
                    json_schema=json_schema,
                    model=model,
                    timeout_sec=timeout_sec,
                )
    raise FatalCallError("unreachable: AsyncRetrying exited without yield")


async def call_text(
    *,
    system_prompt: str,
    user_message: str,
    model: str = "sonnet",
    timeout_sec: int = DEFAULT_TIMEOUT_SEC,
    max_attempts: int = 3,
) -> ModelCallResult:
    """Free-form text continuation (no schema enforcement) — for baselines."""
    return await call(
        system_prompt=system_prompt,
        user_message=user_message,
        json_schema=None,
        model=model,
        timeout_sec=timeout_sec,
        max_attempts=max_attempts,
    )


def current_backend() -> BackendName:
    """Public accessor — useful for logging and the demo's footer."""
    return _resolve_backend()


def load_prompt(path: Path | str) -> str:
    return Path(path).read_text()
