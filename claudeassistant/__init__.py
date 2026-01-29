"""Claude Assistant - A stylish terminal UI for Claude Code."""

from importlib.metadata import version

from claudeassistant.app import ChatApp
from claudeassistant.theme import CHIC_THEME
from claudeassistant.protocols import AgentManagerObserver, AgentObserver, PermissionHandler

__all__ = [
    "ChatApp",
    "CHIC_THEME",
    "AgentManagerObserver",
    "AgentObserver",
    "PermissionHandler",
]
__version__ = version("claudeassistant")
