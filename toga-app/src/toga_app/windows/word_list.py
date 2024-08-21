"""Word List window representation module."""

from urllib.parse import urljoin

import toga
from toga.style import Pack

from toga_app.contrib.http_requests import get_http_response
from toga_app.windows.base import BaseWindow

HOST_API = 'http://127.0.0.1:8000/api/v1/'
URL_PATH = 'words/list/'


class WordListWindow(BaseWindow):
    """Word List window representation."""

    word_list_box: toga.Box
    word_list_table: toga.Table

    def startup(self) -> None:
        """Construct the Word List window."""
        super().startup()

        # Style
        table_style = Pack(
            padding=(14, 7, 0, 7),
        )

        # Table
        self.word_list_table = toga.Table(
            headings=['English word', 'English word'],
            accessors=['eng_word', 'rus_word'],
            style=table_style,
        )

        # Fill Word List box
        self.word_list_box = toga.Box(style=self.main_style)
        self.word_list_box.add(self.btn_goto_main_window)
        self.word_list_box.add(self.btn_get_word_list_data)
        self.word_list_box.add(self.btn_clear_word_list_table)
        self.word_list_box.add(self.word_list_table)

    def goto_word_list_window(self, widget: toga.Widget) -> None:
        """Switch to Word List window."""
        self.main_window.content = self.word_list_box

    ####################################################################
    # handlers
    def fill_word_list_table_handler(
        self,
        widget: toga.Widget,
        **kwargs: object,
    ) -> None:
        """Fill Word List table."""
        self.word_list_table.data = get_http_response(
            urljoin(HOST_API, URL_PATH),
        )

    def clear_word_list_table_handler(
        self,
        widget: toga.Widget,
        **kwargs: object,
    ) -> None:
        """Clean Word List table."""
        self.word_list_table.data.clear()

    ####################################################################
    # buttons
    @property
    def btn_goto_word_list_window(self) -> toga.Button:
        """Button to switch to the Word List window."""
        return toga.Button(
            text='Англо-Русский словарь',
            on_press=self.goto_word_list_window,
        )

    @property
    def btn_get_word_list_data(self) -> toga.Button:
        """Button to get word list data."""
        return toga.Button(
            text='Загрузить список слов',
            on_press=self.fill_word_list_table_handler,
        )

    @property
    def btn_clear_word_list_table(self) -> toga.Button:
        """Button to get word list data."""
        return toga.Button(
            text='Очистить список слов',
            on_press=self.clear_word_list_table_handler,
        )
