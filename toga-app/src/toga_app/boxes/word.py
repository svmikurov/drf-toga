from urllib.parse import urljoin

import toga
from toga import Widget
from toga.style import Pack
from travertino.constants import COLUMN, CENTER

from toga_app.boxes.base import BaseBox

from toga_app.boxes.styled import (
    BoxHeading,
    STYLED_BTN,
    StyledTextInput,
    StyledButton,
)
from toga_app.contrib.http_requests import send_get_request

HOST_API = 'http://127.0.0.1:8000/api/v1/'
LIST_PATH = 'words/list/'


class WordsBox(BaseBox):

    box_heading = BoxHeading(text='Англо-Русский словарь')

    def __init__(self, move_btns) -> None:
        super().__init__()
        self.move_btns = move_btns

        # Table
        self.words_table = toga.Table(
            headings=['По английски', 'По русски'],
            accessors=['eng_word', 'rus_word'],
            style=Pack(
                padding=(14, 7, 7, 7),
                flex=1,
                font_style='italic',
            ),
        )

        # Boxes
        self.line_box1 = BaseBox()

        ################################################################
        # Buttons
        btn_style = STYLED_BTN
        self.btn_update_table = StyledButton(
            'Обновить', on_press=self.update_table_handler
        )
        self.btn_create = toga.Button(
            'Добавить слово', on_press=self.create_handler, style=btn_style
        )
        self.btn_update = toga.Button(
            'Изменить слово',
            on_press=self.update_handler, style=btn_style
        )
        self.btn_delete = toga.Button(
            'Удалить слово', on_press=self.delete_handler, style=btn_style
        )

        ################################################################
        # Add the content on the Words Box
        self.add(
            self.box_heading,
            toga.Box(
                children=[
                    toga.Box(
                        style=Pack(flex=1, direction=COLUMN, alignment=CENTER),
                        children=[
                            self.move_btns.btn_move_main_box,
                            self.move_btns.btn_move_update_word_box,
                        ],
                    ),
                    toga.Box(
                        style=Pack(flex=1, direction=COLUMN, alignment=CENTER),
                        children=[
                            self.move_btns.btn_move_create_word_box,
                            self.btn_delete
                        ]
                    ),
                ],
            ),
            self.words_table,
        )
        self.fill_table()

    ####################################################################
    # Table callback functions
    def update_table_handler(self, widget: Widget):
        self.fill_table()

    ####################################################################
    # Button callback functions
    def create_handler(self, widget: Widget):
        self.fill_table()

    def update_handler(self, widget: Widget):
        self.fill_table()

    def delete_handler(self, widget: Widget):
        self.fill_table()

    ####################################################################
    def fill_table(self):
        self.words_table.data = send_get_request(urljoin(HOST_API, LIST_PATH))


class CreateWordBox(BaseBox):

    box_heading = BoxHeading(text='Добавление слова')

    def __init__(self, move_btns) -> None:
        super().__init__()
        self.move_btns = move_btns

        self.eng_word_input = StyledTextInput(placeholder='Слово на английском')  # noqa: E501
        self.rus_word_input = StyledTextInput(placeholder='Слово на русском')

        self.btn_submit = StyledButton(
            text='Добавить', on_press=self.create_word_handler
        )

        self.add(
            self.box_heading,
            toga.Box(
                children=[
                    toga.Box(
                        style=Pack(flex=1, direction=COLUMN, alignment=CENTER),
                        children=[self.move_btns.btn_move_main_box]
                    ),
                    toga.Box(
                        style=Pack(flex=1, direction=COLUMN, alignment=CENTER),
                        children=[self.move_btns.btn_move_words_box]
                    ),
                ]
            ),
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


class UpdateWordBox(BaseBox):

    box_heading = BoxHeading(text='Добавление слова')

    def __init__(self, move_btns) -> None:
        super().__init__()
        self.move_btns = move_btns

        self.eng_word_input = StyledTextInput(placeholder='Слово на английском')  # noqa: E501
        self.rus_word_input = StyledTextInput(placeholder='Слово на русском')

        self.btn_submit = StyledButton(
            text='Обновить', on_press=self.create_word_handler
        )

        self.add(
            self.box_heading,
            toga.Box(
                children=[
                    toga.Box(
                        style=Pack(flex=1, direction=COLUMN, alignment=CENTER),
                        children=[self.move_btns.btn_move_main_box]
                    ),
                    toga.Box(
                        style=Pack(flex=1, direction=COLUMN, alignment=CENTER),
                        children=[self.move_btns.btn_move_words_box]
                    ),
                ]
            ),
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
