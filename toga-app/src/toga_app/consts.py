"""Constants list."""

from enum import IntEnum

from toga.fonts import SYSTEM_DEFAULT_FONT_SIZE
from toga.style.pack import MONOSPACE

MAIN_WINDOW_SIZE = (300, 500)

SMALL_PADDING = 2

LINE_HEIGHT = 30

FOOTER_FONT_FAMILY = MONOSPACE
SMALL_FONT_SIZE = 10


class FontSize(IntEnum):
    """Font size enum for the Eddington app."""

    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    DEFAULT = 1

    def get_font_size(self) -> int:
        """Get the actual font size from enum value."""
        if self == FontSize.SMALL:
            return 10
        if self == FontSize.MEDIUM:
            return 12
        if self == FontSize.LARGE:
            return 15
        return SYSTEM_DEFAULT_FONT_SIZE

    def get_button_height(self) -> int | None:
        """Get the height of button, related to font size."""
        if self == FontSize.SMALL:
            return 25
        if self == FontSize.MEDIUM:
            return 30
        if self == FontSize.LARGE:
            return 35
        return None
