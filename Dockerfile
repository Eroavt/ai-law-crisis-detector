# Reproducible build for the ALDC artifact.
#
# Provides the Python environment and source tree; does NOT bundle Claude Code
# (which requires user-specific subscription auth). For the `api` backend, pass
# ANTHROPIC_API_KEY via -e or --env-file. For the `claude_code` (Max) backend,
# mount your host's claude binary into the container.

FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    UV_SYSTEM_PYTHON=1

# Install uv (the project manager we use), curl for healthcheck, and minimal CA certs.
RUN apt-get update \
 && apt-get install -y --no-install-recommends curl ca-certificates \
 && rm -rf /var/lib/apt/lists/* \
 && curl -LsSf https://astral.sh/uv/install.sh | sh \
 && mv /root/.local/bin/uv /usr/local/bin/uv

WORKDIR /app
COPY pyproject.toml uv.lock README.md ./
RUN uv sync --frozen --no-dev

COPY src ./src
COPY app ./app
COPY data ./data
COPY scripts ./scripts
COPY docs ./docs
COPY tests ./tests
COPY LICENSE CITATION.cff ./

# Default to the paid-API backend inside the container. Override at run-time to
# claude_code if you've mounted the host CLI binary in.
ENV ALDC_BACKEND=api \
    ALDC_CONCURRENCY=4

EXPOSE 8501
CMD ["uv", "run", "streamlit", "run", "app/demo.py", "--server.address=0.0.0.0", "--server.headless=true"]
