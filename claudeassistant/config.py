"""Configuration management for claudeassistant via ~/.claude/.claudeassistant.yaml."""

import os
import tempfile
from pathlib import Path

import yaml

CONFIG_PATH = Path.home() / ".claude" / ".claudeassistant.yaml"
_OLD_CONFIG_PATH = Path.home() / ".claude" / "claudeassistant.yaml"

_config: dict = {}


def _load_config() -> dict:
    """Load config from disk, creating file atomically if missing."""
    global _config
    if _config:
        return _config

    # Migrate from old config path if it exists and new doesn't
    if not CONFIG_PATH.exists() and _OLD_CONFIG_PATH.exists():
        _OLD_CONFIG_PATH.rename(CONFIG_PATH)
    elif _OLD_CONFIG_PATH.exists():
        # Clean up old config file if new one already exists
        _OLD_CONFIG_PATH.unlink()

    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, encoding="utf-8") as f:
            _config = yaml.safe_load(f) or {}
        # Migrate legacy vim key to vi-mode
        if "vim" in _config:
            _config["vi-mode"] = _config.pop("vim")
            _save_config()
    else:
        # New install - create config with defaults and save
        _config = {
            "recent-tools-expanded": 0,
        }
        _save_config()

    return _config


def _save_config() -> None:
    """Write config to disk atomically."""
    if not _config:
        return
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Atomic write: write to temp file, then rename
    fd, tmp_path = tempfile.mkstemp(dir=CONFIG_PATH.parent, suffix=".yaml")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            yaml.dump(_config, f, default_flow_style=False)
        os.replace(tmp_path, CONFIG_PATH)
    except Exception:
        # Clean up temp file on failure
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


def get_theme() -> str | None:
    """Get saved theme preference, or None if not set."""
    return _load_config().get("theme")


def set_theme(theme: str) -> None:
    """Save theme preference."""
    _load_config()["theme"] = theme
    _save_config()


def get_vi_mode() -> bool:
    """Check if vi mode is enabled."""
    return _load_config().get("vi-mode", False)


def set_vi_mode(enabled: bool) -> None:
    """Enable or disable vi mode."""
    _load_config()["vi-mode"] = enabled
    _save_config()


def get_log_file() -> str | None:
    """Get the log file path, or None if file logging is disabled.

    Defaults to ~/claudeassistant.log. Set to null in config to disable.
    """
    config = _load_config()
    config.setdefault("logging", {})
    return config["logging"].get("file", str(Path.home() / "claudeassistant.log"))


def get_log_notify_level() -> str | None:
    """Get the minimum log level that triggers UI notifications.

    Defaults to 'warning'. Valid values: debug, info, warning, error, critical.
    Set to null/none to disable notifications.
    """
    config = _load_config()
    config.setdefault("logging", {})
    return config["logging"].get("notify-level", "warning")
