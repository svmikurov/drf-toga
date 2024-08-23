from urllib.parse import urljoin

import toga
from toga import Widget
from toga.style import Pack

from toga_app.boxes.base import BaseBox
from toga_app.boxes.styled import BoxHeading, StyledButton
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

        # Buttons
        self.btn_update_table = StyledButton(
            'Обновить таблицу', on_press=self.update_table_handler
        )

        # Add the content on the Words Box
        self.add(
            self.box_heading,
            self.move_btns.btn_move_main_box,
            # self.move_btns.btn_create_word,
            self.btn_update_table,
            self.words_table,
        )
        self.fill_table()

    ####################################################################
    # handlers
    def update_table_handler(self, widget: Widget):
        self.fill_table()
        # End handlers
        ##############

    def fill_table(self):
        self.words_table.data = send_get_request(urljoin(HOST_API, LIST_PATH))
