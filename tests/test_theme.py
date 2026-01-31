"""Tests for theme loading."""

from unittest.mock import patch

from textual.theme import Theme

from claudeassistant.theme import CHIC_THEME, load_custom_themes


def test_default_theme_properties():
    """Default theme has expected properties."""
    assert CHIC_THEME.name == "chic"
    assert CHIC_THEME.primary == "#cc7700"
    assert CHIC_THEME.dark is True


def test_empty_config_returns_no_themes():
    """Empty config returns no custom themes."""
    with patch("claudeassistant.theme.CONFIG", {}):
        themes = load_custom_themes()
        assert themes == []


def test_load_multiple_custom_themes():
    """Multiple custom themes are loaded from config."""
    config = {
        "themes": {
            "dark-red": {"primary": "#ff0000", "dark": True},
            "light-blue": {"primary": "#0000ff", "dark": False},
        }
    }
    with patch("claudeassistant.theme.CONFIG", config):
        themes = load_custom_themes()
        assert len(themes) == 2
        names = {t.name for t in themes}
        assert names == {"dark-red", "light-blue"}


def test_default_color_inheritance():
    """Partial theme definitions inherit defaults from Theme class."""
    config = {"themes": {"minimal": {"primary": "#00ff00"}}}
    with patch("claudeassistant.theme.CONFIG", config):
        themes = load_custom_themes()
        assert len(themes) == 1
        theme = themes[0]
        assert theme.name == "minimal"
        assert theme.primary == "#00ff00"
        # Background should use Theme's default


def test_invalid_theme_entries_skipped():
    """Invalid theme entries (non-dict) are skipped."""
    config = {
        "themes": {
            "valid-theme": {"primary": "#123456"},
            "invalid": "not a dict",
            "also-invalid": 42,
        }
    }
    with patch("claudeassistant.theme.CONFIG", config):
        themes = load_custom_themes()
        assert len(themes) == 1
        assert themes[0].name == "valid-theme"
