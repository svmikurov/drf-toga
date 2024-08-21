"""Mathematical window representation module."""

import toga

from toga_app.windows.base import BaseWindow


class MathematicalWindow(BaseWindow):
    """Mathematical window representation."""

    math_box: toga.Box

    def startup(self) -> None:
        """Construct the Mathematical window representation."""
        super().startup()

        self.math_box = toga.Box(style=self.main_style)

        self.math_box.add(self.btn_goto_main_window)

    def goto_math_window(self, widget: toga.Widget) -> None:
        """Switch to Mathematical window."""
        self.main_window.content = self.math_box

    @property
    def btn_goto_math_window(self) -> toga.Button:
        """Button to switch to the Mathematical window."""
        return toga.Button(
            text='Математические вычисления',
            on_press=self.goto_math_window,
        )
