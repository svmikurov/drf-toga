"""Word List window representation module."""

import toga

from toga_app.windows.base import BaseWindow


class WordListWindow(BaseWindow):
    """Word List window representation."""

    word_list_box: toga.Box

    def startup(self) -> None:
        """Construct the Word List window."""
        super().startup()

        self.word_list_box = toga.Box(style=self.main_style)

        self.word_list_box.add(self.btn_switch_main_window)

    def switch_word_list_window(self, widget: toga.Widget) -> None:
        """Switch to Word List window."""
        self.main_window.content = self.word_list_box

    @property
    def btn_switch_word_list_window(self) -> toga.Button:
        """Button to switch to the Word List window."""
        return toga.Button(
            text='Англо-Русский словарь',
            on_press=self.switch_word_list_window,
        )
