"""Word List window representation module."""

from urllib.parse import urljoin

import toga
from toga import Widget
from toga.style import Pack

from toga_app.contrib.http_requests import (
    send_delete_request,
    send_get_request,
)
from toga_app.windows.base import BaseWindow

HOST_API = 'http://127.0.0.1:8000/api/v1/'
LIST_PATH = 'words/list/'


class WordListWindow(BaseWindow):
    """Word List window representation."""

    word_list_box: toga.Box
    word_list_table: toga.Table
    btn_goto_create_word_window: toga.Button

    def fill_word_list_table(self) -> None:
        """Fill in the table with a list of words."""
        self.word_list_table.data = self.word_list_data

    def startup(self) -> None:
        """Construct the Word List window."""
        super().startup()

        # Table
        self.word_list_table = toga.Table(
            headings=['English word', 'English word'],
            accessors=['eng_word', 'rus_word'],
            style=Pack(
                padding=(14, 7, 7, 7),
                flex=1,  # fill the remaining space with a table
                font_style='italic',
            ),
        )

        # Fill Word List box
        self.word_list_box = toga.Box(
            style=self.main_style,
            children=[
                self.btn_goto_main_window,
                self.btn_goto_create_word_window,
                self.btn_delete_word,
                self.btn_fill_word_list_table,
                self.btn_clear_word_list_table,
                self.word_list_table,
            ],
        )

    @property
    def word_list_data(self) -> list[dict]:
        """Word list."""
        return send_get_request(urljoin(HOST_API, LIST_PATH))

    def goto_word_list_window(self, widget: Widget) -> None:
        """Switch to Word List window."""
        self.fill_word_list_table()
        self.main_window.content = self.word_list_box

    ####################################################################
    # handlers
    def fill_word_list_handler(
            self, widget: Widget, **kwargs: object
    ) -> None:
        """Fill word list table handler."""
        self.fill_word_list_table()

    def clear_word_list_handler(
        self, widget: Widget, **kwargs: object
    ) -> None:
        """Clear word list table handler."""
        self.word_list_table.data.clear()

    def delete_word_handler(
        self, widget: toga.Widget, **kwargs: object
    ) -> None:
        """Delete word handler."""
        if self.word_list_table.selection:
            delete_word_pk = self.word_list_table.selection.pk
            response = send_delete_request(
                url=urljoin(HOST_API, f'words/delete/{delete_word_pk}/')
            )
            self.main_window.info_dialog(
                title='Результат отправки запроса',
                message=response,
            )
            self.fill_word_list_table()
        else:
            print('Выберите слово!')

    ####################################################################
    # buttons
    @property
    def btn_goto_word_list_window(self) -> toga.Button:
        """Go to Word List window button."""
        return toga.Button(
            text='Англо-Русский словарь',
            on_press=self.goto_word_list_window,
        )

    @property
    def btn_fill_word_list_table(self) -> toga.Button:
        """Button to fill word list table."""
        return toga.Button(
            text='Загрузить список слов',
            on_press=self.fill_word_list_handler,
        )

    @property
    def btn_clear_word_list_table(self) -> toga.Button:
        """Button to clear word list table."""
        return toga.Button(
            text='Очистить список слов',
            on_press=self.clear_word_list_handler,
        )

    @property
    def btn_delete_word(self) -> toga.Button:
        """Button to delete word."""
        return toga.Button(
            text='Удалить слово',
            on_press=self.delete_word_handler,
        )
