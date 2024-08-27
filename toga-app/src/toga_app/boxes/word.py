"""Word boxes."""

import toga
from toga import Widget
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
    send_post_request,
    send_put_request,
)
from toga_app.move_btns import BoxButtons

WORDS_PATH = 'api/v1/words/'


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

        self.btn_delete = StyledButton(
            'Удалить слово',
            on_press=self.delete_handler,
        )

        # Create navigation box
        self.nav_box = toga.Box()
        self.left_box = PartSplitBox()
        self.right_box = PartSplitBox()

        # Build widget tree
        self.add(
            self.nav_box,
            self.words_table,
        )
        self.nav_box.add(self.left_box, self.right_box)
        self.left_box.add(
            self.move_btns.btn_move_main_box,
            self.move_btns.btn_move_update_word_box,
        )
        self.right_box.add(
            self.move_btns.btn_move_create_word_box,
            self.btn_delete,
        )

    ####################################################################
    # Button callback functions
    def delete_handler(self, widget: Widget) -> None:
        """Delete word."""
        delete_path = f'{WORDS_PATH}{self.words_table.selection.pk}/'
        response = send_delete_request(delete_path)
        self.fill_table()
        self.window.info_dialog(title='Сообщение:', message=response)

    ####################################################################
    def fill_table(self) -> None:
        """Fill the Word Table box."""
        self.words_table.data = send_get_request(WORDS_PATH)


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
        payload = {
            'eng_word': self.eng_word_input.value,
            'rus_word': self.rus_word_input.value,
        }
        response = send_post_request(path=WORDS_PATH, payload=payload)
        self.window.info_dialog(title='Сообщение:', message=str(response))
        self.eng_word_input.value = None
        self.rus_word_input.value = None


class UpdateWordBox(BaseBox):
    """Update Word Box."""

    box_heading = BoxHeading(text='Добавление слова')
    word_pk = None

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
        payload = {
            'eng_word': self.eng_word_input.value,
            'rus_word': self.rus_word_input.value,
        }
        update_path = f'{WORDS_PATH}{self.word_pk}/'
        response = send_put_request(update_path, payload=payload)
        self.window.info_dialog(
            title='Результат отправки запроса',
            message=response,
        )
        self.eng_word_input.value = None
        self.rus_word_input.value = None
        self.app.to_words_box()
