"""Row box."""

from toga import Widget
from toga.style import Pack
from toga.style.pack import CENTER, ROW

from toga_app.boxes.base import BaseBox
from toga_app.consts import LINE_HEIGHT, SMALL_PADDING


class LineBox(BaseBox):
    """Visual box representing a horizontal row."""

    def __init__(
        self,
        height: int = LINE_HEIGHT,
        alignment: str = CENTER,
        padding_left: int = SMALL_PADDING,
        padding_right: int = SMALL_PADDING,
        padding_top: int = SMALL_PADDING,
        padding_bottom: int = SMALL_PADDING,
        children: Widget | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize box."""
        super().__init__(
            style=Pack(
                direction=ROW,
                height=height,
                alignment=alignment,
                padding_left=padding_left,
                padding_right=padding_right,
                padding_top=padding_top,
                padding_bottom=padding_bottom,
                **kwargs,
            ),
            children=children,
        )
