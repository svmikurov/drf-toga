import toga
from toga import TextInput

from toga_app.boxes.base import BaseBox
from toga_app.boxes.components.labels import BoxHeading
from toga_app.move_btns import Buttons

HOST_API = 'http://127.0.0.1:8000/api/v1/'
URL_PATH = 'words/list/'


class CreateWordBox(Buttons, BaseBox):

    box_heading = BoxHeading(
        text='Добавление слова',
    )

    def __init__(self, move_btn_callbacks: dict) -> None:
        super().__init__()
        self.move_btn_callbacks = move_btn_callbacks

        self.eng_word_input = TextInput(placeholder='Слово на английском')
        self.rus_word_input = TextInput(placeholder='Слово на русском')

        self.btn_submit = toga.Button(
            text='Добавить',
            on_press=self.create_word_handler,
        )

        self.add(
            self.box_heading,
            self.btn_move_main_box,
            self.btn_move_words_box,
            self.eng_word_input,
            self.rus_word_input,
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
