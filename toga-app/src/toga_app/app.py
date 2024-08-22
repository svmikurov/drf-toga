"""Learn Toga widget toolkit application."""

import toga

from toga_app.windows.base import BaseWindow
from toga_app.windows.english.word_create import CreateWordWindow
from toga_app.windows.english.word_list import WordListWindow
from toga_app.windows.mathematical import MathematicalWindow


class TogaApp(
    WordListWindow,
    MathematicalWindow,
    CreateWordWindow,
    BaseWindow,
    toga.App,
):
    """Simple Toga application."""

    def startup(self) -> None:
        """Construct Main window consider other windows."""
        super().startup()

        self.main_box = toga.Box(style=self.main_style)
        self.main_box.add(self.btn_goto_word_list_window)
        self.main_box.add(self.btn_goto_math_window)

        self.main_window.content = self.main_box
        self.main_window.show()


def main() -> toga.App:
    """Return Toga app."""
    return TogaApp()
