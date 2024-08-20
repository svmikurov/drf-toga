"""Learn Toga widget toolkit application."""

import toga

from toga_app.windows.mathematical import MathematicalWindow
from toga_app.windows.word_list import WordListWindow


class TogaApp(
    WordListWindow,
    MathematicalWindow,
):
    """Simple Toga application."""

    def startup(self) -> None:
        """Construct Main window consider other windows."""
        super().startup()
        self.main_box.add(self.btn_switch_word_list_window)
        self.main_box.add(self.btn_switch_math_window)


def main() -> toga.App:
    """Return Toga app."""
    return TogaApp()
