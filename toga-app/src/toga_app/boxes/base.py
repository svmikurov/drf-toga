"""Application Base Box."""

import toga
from toga.style import Pack
from travertino.constants import COLUMN, ROW


class BaseBox(toga.Box):
    """Class representing the base box of the application."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize box."""
        super().__init__(*args, **kwargs)
        self.style = Pack(flex=1, direction=COLUMN)


class LineBox(toga.Box):
    """Line box."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.style = Pack(direction=ROW)
