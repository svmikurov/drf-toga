"""Word boxes."""

from urllib.parse import urljoin

import toga
from toga import Widget, App
from toga.style import Pack
from travertino.constants import CENTER, COLUMN, ITALIC

from toga_app.boxes.base import BaseBox
from toga_app.boxes.styled import (
    BoxHeading,
    PartSplitBox,
    StyledButton,
    StyledTextInput,
)
from toga_app.contrib.http_requests import (
    send_delete_request,
    send_get_request,
)
from toga_app.move_btns import BoxButtons

HOST_API = 'http://127.0.0.1:8000/api/v1/'
WORDS_PATH = 'words/'


class WordsBox(BaseBox):
    """Words Box."""

    box_heading = BoxHeading(text='Англо-Русский словарь')

    def __init__(self, move_btns: BoxButtons) -> None:
        """Construct the Words Box."""
        super().__init__()
        self.move_btns = move_btns

        # Table
        self.words_table = toga.Table(
            headings=['По английски', 'По русски'],
            accessors=['eng_word', 'rus_word'],
            style=Pack(
                padding=(14, 7, 7, 7),
                flex=1,
                font_style=ITALIC,
            ),
        )

        # Boxes
        self.line_box1 = BaseBox()

        ################################################################
        # Buttons
        self.btn_delete = StyledButton(
            'Удалить слово',
            on_press=self.delete_handler,
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
                            self.btn_delete,
                        ],
                    ),
                ],
            ),
            self.words_table,
        )

    def __call__(self, *args, **kwargs):
        self.fill_table()

    ####################################################################
    # Table callback functions
    def update_table_handler(self, widget: Widget) -> None:
        """Update Word List table."""
        self.fill_table()

    ####################################################################
    # Button callback functions
    def create_handler(self, widget: Widget) -> None:
        """Create word."""
        self.fill_table()

    def update_handler(self, widget: Widget) -> None:
        """Update word."""
        self.fill_table()

    def delete_handler(self, widget: Widget) -> None:
        """Delete word."""
        word_pk = f'{self.words_table.selection.pk}/'
        delete_path = urljoin(WORDS_PATH, word_pk)
        url = urljoin(HOST_API, delete_path)
        response = send_delete_request(url)
        self.fill_table()
        self.window.info_dialog(title='Сообщение:', message=response)

    ####################################################################
    def fill_table(self) -> None:
        """Fill the Word Table box."""
        self.words_table.data = send_get_request(urljoin(HOST_API, WORDS_PATH))


class CreateWordBox(BaseBox):
    """Create Word Bpx."""

    box_heading = BoxHeading(text='Добавление слова')

    def __init__(self, move_btns: BoxButtons) -> None:
        """Construct the Create Word box."""
        super().__init__()
        self.move_btns = move_btns

        self.eng_word_input = StyledTextInput(
            placeholder='Слово на английском'
        )  # noqa: E501
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
                        children=[self.move_btns.btn_move_main_box],
                    ),
                    toga.Box(
                        style=Pack(flex=1, direction=COLUMN, alignment=CENTER),
                        children=[self.move_btns.btn_move_words_box],
                    ),
                ]
            ),
            self.eng_word_input,
            self.rus_word_input,
            self.btn_submit,
        )

    def create_word_handler(self, widget: toga.Widget) -> None:
        """Add Word to English-Russian dictionary."""
        # data = {
        #     'eng_word': self.eng_word_input.value,
        #     'rus_word': self.rus_word_input.value,
        # }
        # response = send_post_request(
        #     url=urljoin(HOST_API, URL_PATH),
        #     data=data,
        # )
        self.window.info_dialog(
            title='Результат отправки запроса',
            message='response',
        )


class UpdateWordBox(BaseBox):
    """Update Word Box."""

    box_heading = BoxHeading(text='Добавление слова')

    def __init__(self, move_btns: BoxButtons) -> None:
        """Construct the Update Word Box."""
        super().__init__()
        self.move_btns = move_btns

        self.btns_split_box = toga.Box()
        self.left_box = PartSplitBox()
        self.right_box = PartSplitBox()

        self.btns_split_box.add(self.right_box, self.left_box)
        self.right_box.insert(0, self.move_btns.btn_move_main_box)
        self.left_box.insert(0, self.move_btns.btn_move_words_box)

        self.eng_word_input = StyledTextInput(
            placeholder='Слово на английском'
        )  # noqa: E501
        self.rus_word_input = StyledTextInput(placeholder='Слово на русском')

        self.btn_submit = StyledButton(
            text='Обновить', on_press=self.word_handler
        )

        self.add(
            self.box_heading,
            self.btns_split_box,
            self.eng_word_input,
            self.rus_word_input,
            self.btn_submit,
        )

    def word_handler(self, widget: toga.Widget) -> None:
        """Add Word to English-Russian dictionary."""
        # data = {
        #     'eng_word': self.eng_word_input.value,
        #     'rus_word': self.rus_word_input.value,
        # }
        # response = send_post_request(
        #     url=urljoin(HOST_API, URL_PATH),
        #     data=data,
        # )
        self.window.info_dialog(
            title='Результат отправки запроса',
            message='response',
        )
