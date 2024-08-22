"""Application Base Box."""

import toga


class BaseBox(toga.Box):
    """Class representing the base box of the application."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize box."""
        super().__init__(*args, **kwargs)
