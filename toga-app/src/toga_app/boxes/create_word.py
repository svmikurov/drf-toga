from urllib.parse import urljoin

import toga
from toga.style import Pack
from travertino.constants import COLUMN

from toga_app.boxes.base import BaseBox
from toga_app.contrib.http_requests import send_post_request

HOST_API = 'http://127.0.0.1:8000/api/v1/'
URL_PATH = 'words/list/'


class CreateWordBox(BaseBox):

    def __init__(self, move_buttons: dict) -> None:
        super().__init__()
        self.move_buttons = move_buttons
        self.style = Pack(flex=1, direction=COLUMN)

        eng_word_label = toga.Label(text='Введите слово на английском')
        self.eng_word_input = toga.TextInput()
        rus_word_label = toga.Label(text='Введите слово на русском')
        self.rus_word_input = toga.TextInput()

        self.btn_submit = toga.Button(
            text='Добавить',
            on_press=self.create_word_handler,
        )
        self.btn_move_main_box = toga.Button(
            'На главную',
            on_press=lambda _: self.move_buttons['main_box'](),
        )
        self.btn_move_words_box = toga.Button(
            'Англо-Русский словарь',
            on_press=lambda _: self.move_buttons['words_box'](),
        )

        self.add(
            self.btn_move_main_box,
            self.btn_move_words_box,
            eng_word_label, self.eng_word_input,
            rus_word_label, self.rus_word_input,
            self.btn_submit
        )

    def create_word_handler(self, widget: toga.Widget) -> None:
        """Add Word to English-Russian dictionary."""
        data = {
            'eng_word': self.eng_word_input.value,
            'rus_word': self.rus_word_input.value,
        }
        # response = send_post_request(
        #     url=urljoin(HOST_API, URL_PATH),
        #     data=data,
        # )
        self.window.info_dialog(
            title='Результат отправки запроса',
            message='response',
        )
