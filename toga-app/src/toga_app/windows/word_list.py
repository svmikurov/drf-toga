"""Word List window representation module."""
from urllib.parse import urljoin

import httpx
import toga
from toga.style import Pack

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
        table_style = Pack(
            padding=(14, 7, 0, 7),
        )

        self.word_list_box = toga.Box(style=self.main_style)

        self.word_list_table = toga.Table(
            headings=['English word', 'English word'],
            accessors=['eng_word', 'rus_word'],
            style=table_style,
        )

        self.word_list_box.add(self.btn_switch_main_window)
        self.word_list_box.add(self.btn_get_word_list_data)
        self.word_list_box.add(self.btn_clear_word_list_table)
        self.word_list_box.add(self.word_list_table)

    def switch_word_list_window(self, widget: toga.Widget) -> None:
        """Switch to Word List window."""
        self.main_window.content = self.word_list_box

    @staticmethod
    def get_word_list_data() -> dict:
        """Get Word List data."""
        with httpx.Client() as client:
            response = client.get(url=urljoin(HOST_API, URL_PATH))
        payload = response.json()
        return payload

    @property
    def btn_switch_word_list_window(self) -> toga.Button:
        """Button to switch to the Word List window."""
        return toga.Button(
            text='Англо-Русский словарь',
            on_press=self.switch_word_list_window,
        )

    def fill_word_list_table_handler(self, widget, **kwargs):
        self.word_list_table.data = self.get_word_list_data()

    def clear_word_list_table_handler(self, widget, **kwargs):
        self.word_list_table.data.clear()

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
