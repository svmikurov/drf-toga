"""Add new word to English-Russian dictionary module."""

from urllib.parse import urljoin

import toga

from toga_app.contrib.http_requests import send_post_request
from toga_app.windows.base import BaseWindow

HOST_API = 'http://127.0.0.1:8000/api/v1/'
URL_PATH = 'words/list/'


class CreateWordWindow(BaseWindow):
    """Add New Word window representation."""

    create_word_box = toga.Box
    btn_goto_word_list_window: toga.Button
    eng_word_input: toga.TextInput
    rus_word_input: toga.TextInput

    def startup(self) -> None:
        """Construct the Add New Word window."""
        super().startup()

        eng_word_label = toga.Label(text='Введите слово на английском')
        self.eng_word_input = toga.TextInput()
        rus_word_label = toga.Label(text='Введите слово на русском')
        self.rus_word_input = toga.TextInput()

        self.create_word_box = toga.Box(
            style=self.main_style,
            children=[
                self.btn_goto_word_list_window,
                eng_word_label,
                self.eng_word_input,
                rus_word_label,
                self.rus_word_input,
                self.btn_create_word,
            ],
        )

    def goto_create_word_window(self, widget: toga.Widget) -> None:
        """Go to Create Word window."""
        self.main_window.content = self.create_word_box

    ####################################################################
    # handlers
    def create_word_handler(self, widget: toga.Widget) -> None:
        """Add Word to English-Russian dictionary."""
        data = {
            'eng_word': self.eng_word_input.value,
            'rus_word': self.rus_word_input.value,
        }
        response = send_post_request(
            url=urljoin(HOST_API, URL_PATH),
            data=data,
        )
        self.main_window.info_dialog(
            title='Результат отправки запроса',
            message=response,
        )

    ####################################################################
    # buttons
    @property
    def btn_goto_create_word_window(self) -> toga.Button:
        """Go to Add Word window button."""
        return toga.Button(
            text='Добавить слово',
            on_press=self.goto_create_word_window,
        )

    @property
    def btn_create_word(self) -> toga.Button:
        """Add Word to English-Russian dictionary button."""
        return toga.Button(
            text='Добавить слово в словарь',
            on_press=self.create_word_handler,
        )
