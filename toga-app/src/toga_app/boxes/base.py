"""Application Base Box."""

import toga
from toga.style import Pack
from travertino.constants import COLUMN, ROW


class BaseBox(toga.Box):
    """Class representing the base box of the application."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Initialize box."""
        super().__init__(*args, **kwargs)
        self.style = Pack(flex=1, direction=COLUMN)


class LineBox(toga.Box):
    """Line Box widget."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the Line Box widget."""
        super().__init__(*args, **kwargs)
        self.style = Pack(direction=ROW)
