"""Textual widgets for Claude Code UI.

Re-exports all widgets from submodules for backward compatibility.
"""

# Base classes
from claudeassistant.widgets.base import ToolWidget

# Primitives
from claudeassistant.widgets.primitives import (
    Button,
    QuietCollapsible,
    AutoHideScroll,
    Spinner,
)

# Content widgets
from claudeassistant.widgets.content import (
    ChatMessage,
    ChatInput,
    ThinkingIndicator,
    ImageAttachments,
    ErrorMessage,
    SystemInfo,
    ChatAttachment,
    ToolUseWidget,
    TaskWidget,
    AgentToolWidget,
    AgentListWidget,
    ShellOutputWidget,
    PendingShellWidget,
    EditPlanRequested,
    DiffWidget,
    TodoWidget,
    TodoPanel,
)

# Input widgets
from claudeassistant.widgets.input import TextAreaAutoComplete, HistorySearch

# Layout widgets
from claudeassistant.widgets.layout import (
    ChatView,
    AgentItem,
    AgentSection,
    PlanItem,
    PlanSection,
    FileItem,
    FilesSection,
    SidebarSection,
    SidebarItem,
    HamburgerButton,
    SessionItem,
    AutoEditLabel,
    ModelLabel,
    StatusFooter,
    IndicatorWidget,
    CPUBar,
    ContextBar,
    ProcessIndicator,
    ProcessPanel,
    ProcessItem,
)

# Base re-exports (ClickableLabel used by layout widgets)
from claudeassistant.widgets.base import ClickableLabel

# Data classes (re-exported for convenience)
from claudeassistant.processes import BackgroundProcess

# Report widgets
from claudeassistant.widgets.reports import ContextReport

# Modal screens
from claudeassistant.widgets.modals import ProfileModal, ProcessModal

# Prompts
from claudeassistant.widgets.prompts import (
    BasePrompt,
    SelectionPrompt,
    QuestionPrompt,
    ModelPrompt,
)

__all__ = [
    # Base
    "ToolWidget",
    # Primitives
    "Button",
    "QuietCollapsible",
    "AutoHideScroll",
    "Spinner",
    # Content
    "ChatMessage",
    "ChatInput",
    "ThinkingIndicator",
    "ImageAttachments",
    "ErrorMessage",
    "SystemInfo",
    "ChatAttachment",
    "ToolUseWidget",
    "TaskWidget",
    "AgentToolWidget",
    "AgentListWidget",
    "ShellOutputWidget",
    "PendingShellWidget",
    "EditPlanRequested",
    "DiffWidget",
    "TodoWidget",
    "TodoPanel",
    # Input
    "TextAreaAutoComplete",
    "HistorySearch",
    # Layout
    "ChatView",
    "AgentItem",
    "AgentSection",
    "SessionItem",
    "PlanItem",
    "PlanSection",
    "FileItem",
    "FilesSection",
    "SidebarSection",
    "SidebarItem",
    "HamburgerButton",
    "ClickableLabel",
    "AutoEditLabel",
    "ModelLabel",
    "StatusFooter",
    "IndicatorWidget",
    "CPUBar",
    "ContextBar",
    "ProcessIndicator",
    "ProcessPanel",
    "ProcessItem",
    "BackgroundProcess",
    # Reports
    "ContextReport",
    # Modals
    "ProfileModal",
    "ProcessModal",
    # Prompts
    "BasePrompt",
    "SelectionPrompt",
    "QuestionPrompt",
    "ModelPrompt",
]
