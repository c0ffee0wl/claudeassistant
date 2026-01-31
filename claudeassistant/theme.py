"""Theme definition for Claude Assistant.

Custom themes can be defined in ~/.claude/.claudeassistant.yaml:

    themes:
      my-theme:
        primary: "#ff0000"
        background: "#000000"
        dark: true
"""

from textual.theme import Theme

from claudeassistant.config import CONFIG


def load_custom_themes() -> list[Theme]:
    """Load custom themes from config.

    Define themes in ~/.claude/.claudeassistant.yaml:
        themes:
          my-theme:
            primary: "#ff0000"
            background: "#000000"
            dark: true
    """
    themes_config = CONFIG.get("themes", {})
    custom_themes = []
    for name, colors in themes_config.items():
        if not isinstance(colors, dict):
            continue
        theme = Theme(name=name, **colors)
        custom_themes.append(theme)
    return custom_themes


# Custom theme for Claude Assistant
CHIC_THEME = Theme(
    name="chic",
    primary="#cc7700",
    secondary="#5599dd",  # Sky blue for syntax highlighting
    accent="#445566",
    background="black",
    surface="#111111",
    panel="#555555",  # Used for borders and subtle UI elements
    success="#5599dd",  # Same as secondary - strings in code
    warning="#aaaa00",  # Yellow - moderate usage/caution
    error="#cc3333",  # Red - high usage/errors
    dark=True,
)
