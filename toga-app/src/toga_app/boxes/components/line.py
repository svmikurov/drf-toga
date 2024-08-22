"""Row box."""
from toga.style import Pack
from toga.style.pack import CENTER, ROW

from toga_app.boxes.base import BaseBox
from toga_app.consts import LINE_HEIGHT, SMALL_PADDING


class LineBox(BaseBox):
    """Visual box representing a horizontal row."""

    def __init__(
        self,
        height=LINE_HEIGHT,
        alignment=CENTER,
        padding_left=SMALL_PADDING,
        padding_right=SMALL_PADDING,
        padding_top=SMALL_PADDING,
        padding_bottom=SMALL_PADDING,
        children=None,
        **kwargs,
    ):
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
