import toga
from toga.style import Pack


class BoxHeading(toga.Label):

    def __init__(self, **kwargs):
        super().__init__(
            style=Pack(
                padding_left=7,
                padding_right=7,
                padding_top=7,
                padding_bottom=7,
            ),
            **kwargs
        )
