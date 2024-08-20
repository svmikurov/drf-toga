"""Word List window representation module."""

import toga
from toga.style import Pack

from toga_app.windows.base import BaseWindow


class WordListWindow(BaseWindow):
    """Word List window representation."""

    word_list_box: toga.Box

    def startup(self) -> None:
        """Construct the Word List window."""
        super().startup()
        table_style = Pack(
            padding=(14, 7, 0, 7),
        )

        self.word_list_box = toga.Box(style=self.main_style)

        table_dict = toga.Table(
            headings=['English word', 'English word'],
            accessors=['eng_word', 'rus_word'],
            data=[
                {'eng_word': 'black', 'rus_word': 'черный'},
                {'eng_word': 'red', 'rus_word': 'красный'},
                {'eng_word': 'blue', 'rus_word': 'синий'},
            ],
            style=table_style,
        )

        self.word_list_box.add(self.btn_switch_main_window)
        self.word_list_box.add(table_dict)

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
