"""Totality test for legal_map: every declared LegalAxisTag must have a mapping."""

from aldc.legal_map import all_tags, assert_total, get


def test_total_coverage() -> None:
    assert_total()


def test_each_tag_has_required_fields() -> None:
    required = {
        "primary_article",
        "secondary_articles",
        "leading_case",
        "doctrinal_claim",
        "paper_section",
        "exhibit_id",
    }
    for tag in all_tags():
        mapping = get(tag)
        assert required <= set(mapping.keys()), f"{tag} missing fields"
        assert mapping["primary_article"], f"{tag} has empty primary_article"
        assert mapping["doctrinal_claim"], f"{tag} has empty doctrinal_claim"
