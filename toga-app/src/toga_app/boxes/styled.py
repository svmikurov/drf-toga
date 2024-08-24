"""Styled widgets."""

import toga
from toga.style import Pack
from travertino.constants import BOLD, CENTER, COLUMN

from toga_app.consts import SMALL_PADDING

HEIGHT = 40
PADDING_TOP = SMALL_PADDING
PADDING_RIGHT = SMALL_PADDING * 2
PADDING_BOTTOM = SMALL_PADDING
PADDING_LEFT = SMALL_PADDING * 2
NO_PADDING = 0

STYLED_BTN = Pack(
    padding_top=PADDING_TOP,
    padding_right=PADDING_RIGHT,
    padding_bottom=PADDING_BOTTOM,
    padding_left=PADDING_LEFT,
    height=HEIGHT,
)


class BoxHeading(toga.Label):
    """Box Heading widget."""

    def __init__(
        self,
        text: str,
        *,
        padding_left: int = PADDING_LEFT,
        padding_right: int = PADDING_RIGHT,
        padding_top: int = PADDING_TOP,
        padding_bottom: int = PADDING_BOTTOM,
        text_align: str = CENTER,
        font_weight: str = BOLD,
        **kwargs: object,
    ) -> None:
        """Construct The Box Heading widget."""
        super().__init__(
            text=text,
            style=Pack(
                padding_left=padding_left,
                padding_right=padding_right,
                padding_top=padding_top,
                padding_bottom=padding_bottom,
                text_align=text_align,
                font_weight=font_weight,
            ),
            **kwargs,
        )


class StyledButton(toga.Button):
    """Styled Button widget."""

    def __init__(
        self,
        text: str | None = None,
        *,
        padding_left: int = PADDING_LEFT,
        padding_right: int = PADDING_RIGHT,
        padding_top: int = PADDING_TOP,
        padding_bottom: int = PADDING_BOTTOM,
        height: int = HEIGHT,
        **kwargs: object,
    ) -> None:
        """Construct the Styled Button widget."""
        super().__init__(
            text=text,
            style=Pack(
                padding_left=padding_left,
                padding_right=padding_right,
                padding_top=padding_top,
                padding_bottom=padding_bottom,
                height=height,
            ),
            **kwargs,
        )


class StyledTextInput(toga.TextInput):
    """Styled Text Input widget."""

    def __init__(
        self,
        *,
        padding_left: int = PADDING_LEFT,
        padding_right: int = PADDING_RIGHT,
        padding_top: int = PADDING_TOP,
        padding_bottom: int = PADDING_BOTTOM,
        height: int = HEIGHT,
        **kwargs: object,
    ) -> None:
        """Construct the Styled Text Input widget."""
        super().__init__(
            style=Pack(
                padding_left=padding_left,
                padding_right=padding_right,
                padding_top=padding_top,
                padding_bottom=padding_bottom,
                height=height,
            ),
            **kwargs,
        )


class PartSplitBox(toga.Box):
    """Box for insertion into a split box."""

    def __init__(
        self,
        *args: object,
        padding_left: int = NO_PADDING,
        padding_right: int = NO_PADDING,
        **kwargs: object,
    ) -> None:
        """Construct the box."""
        super().__init__(*args, **kwargs)
        self.style = Pack(
            flex=1,
            padding_left=padding_left,
            padding_right=padding_right,
            direction=COLUMN,
            alignment=CENTER,
        )
