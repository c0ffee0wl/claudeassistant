"""Configuration management for claudeassistant via ~/.claude/.claudeassistant.yaml."""

import os
import tempfile
from pathlib import Path

import yaml

CONFIG_PATH = Path.home() / ".claude" / ".claudeassistant.yaml"
_OLD_CONFIG_PATH = Path.home() / ".claude" / "claudeassistant.yaml"


def _load() -> tuple[dict, bool]:
    """Load config from disk, creating file atomically if missing.

    Returns:
        Tuple of (config dict, is_new_install)
    """
    new_install = False

    # Migrate from old config path if it exists and new doesn't
    if not CONFIG_PATH.exists() and _OLD_CONFIG_PATH.exists():
        _OLD_CONFIG_PATH.rename(CONFIG_PATH)
    elif _OLD_CONFIG_PATH.exists():
        # Clean up old config file if new one already exists
        _OLD_CONFIG_PATH.unlink()

    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, encoding="utf-8") as f:
            config = yaml.safe_load(f) or {}
        # Migrate legacy vim key to vi-mode
        if "vim" in config:
            config["vi-mode"] = config.pop("vim")
            _save(config)
    else:
        # New install - create config with defaults and save
        new_install = True
        config = {
            "recent-tools-expanded": 0,
        }
        _save(config)

    return config, new_install


def _save(config: dict) -> None:
    """Write config to disk atomically."""
    if not config:
        return
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Atomic write: write to temp file, then rename
    fd, tmp_path = tempfile.mkstemp(dir=CONFIG_PATH.parent, suffix=".yaml")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            yaml.dump(config, f, default_flow_style=False)
        os.replace(tmp_path, CONFIG_PATH)
    except Exception:
        # Clean up temp file on failure
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


# Load config once at module import
CONFIG, NEW_INSTALL = _load()


def save() -> None:
    """Save the CONFIG dict to disk."""
    _save(CONFIG)
