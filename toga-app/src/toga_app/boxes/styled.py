from toga.style import Pack

import toga
from travertino.constants import BOLD, CENTER

from toga_app.consts import SMALL_PADDING

HEIGHT = 40
PADDING_TOP = SMALL_PADDING
PADDING_RIGHT = SMALL_PADDING * 2
PADDING_BOTTOM = SMALL_PADDING
PADDING_LEFT = SMALL_PADDING * 2


class BoxHeading(toga.Label):

    def __init__(
        self,
        text: str,
        *,
        padding_left=PADDING_LEFT,
        padding_right=PADDING_RIGHT,
        padding_top=PADDING_TOP,
        padding_bottom=PADDING_BOTTOM,
        text_align=CENTER,
        font_weight=BOLD,
        **kwargs,
    ):
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
            **kwargs
        )


class StyledButton(toga.Button):

    def __init__(
        self,
        text: str | None = None,
        *,
        padding_left=PADDING_LEFT,
        padding_right=PADDING_RIGHT,
        padding_top=PADDING_TOP,
        padding_bottom=PADDING_BOTTOM,
        height=HEIGHT,
        **kwargs,
    ):
        super().__init__(
            text=text,
            style=Pack(
                padding_left=padding_left,
                padding_right=padding_right,
                padding_top=padding_top,
                padding_bottom=padding_bottom,
                height=height,
            ),
            **kwargs
        )


class StyledTextInput(toga.TextInput):

    def __init__(
        self,
        *,
        padding_left=PADDING_LEFT,
        padding_right=PADDING_RIGHT,
        padding_top=PADDING_TOP,
        padding_bottom=PADDING_BOTTOM,
        height=HEIGHT,
        **kwargs,
    ):
        super().__init__(
            style=Pack(
                padding_left=padding_left,
                padding_right=padding_right,
                padding_top=padding_top,
                padding_bottom=padding_bottom,
                height=height,
            ),
            **kwargs
        )