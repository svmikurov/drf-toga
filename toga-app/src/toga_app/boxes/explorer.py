"""Explore Liskov Substitution Principle."""

import toga
from toga.style import Pack

DEFAULT_STYLE = Pack()


class ExploreLSPButton(toga.Button):
    """Explore LSP Box."""

    def __init__(
        self,
        *args: object,
        style: object | None = None,
        **kwargs: object,
    ) -> None:
        """Construct."""
        self.style = style if style else DEFAULT_STYLE
        super().__init__(*args, style, **kwargs)


class ExploreLSPBox(toga.Box):
    """Explore LSP Box."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct."""
        super().__init__()

        # Define Button
        self.btn_move_main_box = ExploreLSPButton(
            'На главную',
            on_press=lambda _: self.app.to_main_box(),
        )

        # Add Button into ExploreLSPBox
        self.add(self.btn_move_main_box)
