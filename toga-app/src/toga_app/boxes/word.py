"""Word boxes."""

import toga
from toga import Widget
from toga.style import Pack
from travertino.constants import CENTER, COLUMN, ITALIC

from toga_app.boxes.base import BaseBox
from toga_app.boxes.styled import (
    HALF_SMALL_PADDING,
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
            headings=['ID', 'По английски', 'По русски'],
            accessors=['pk', 'eng_word', 'rus_word'],
            style=Pack(
                padding=(14, 7, 7, 7),
                flex=1,
                font_style=ITALIC,
            ),
        )

        # Buttons
        self.btn_update = StyledButton(
            'Изменить',
            on_press=self.update_handler,
            padding_right=HALF_SMALL_PADDING,
        )
        self.btn_delete = StyledButton(
            'Удалить',
            on_press=self.delete_handler,
            padding_left=HALF_SMALL_PADDING,
        )
        self.btn_next_pagination_url = toga.Button(
            '>>',
            on_press=self.next_words_handler,
        )
        self.btn_previous_pagination_url = toga.Button(
            '<<',
            on_press=self.previous_words_handler,
        )

        # Create boxes
        self.nav_box = toga.Box()
        self.left_box = PartSplitBox()
        self.right_box = PartSplitBox()
        self.pagination_box = toga.Box()

        # Build widget tree
        self.add(
            self.nav_box,
            self.words_table,
            self.pagination_box,
        )
        self.nav_box.add(self.left_box, self.right_box)
        self.left_box.add(
            self.move_btns.btn_move_main_box,
            self.btn_update,
        )
        self.right_box.add(
            self.move_btns.btn_move_create_word_box,
            self.btn_delete,
        )
        self.pagination_box.add(
            toga.Box(style=Pack(flex=1)),  # Spacer
            self.btn_previous_pagination_url,
            self.btn_next_pagination_url,
            toga.Box(style=Pack(flex=1)),  # Spacer
        )

    ####################################################################
    # Button callback functions
    def delete_handler(self, widget: Widget) -> None:
        """Delete word."""
        try:
            delete_path = f'{WORDS_PATH}{self.words_table.selection.pk}/'
            response = send_delete_request(delete_path)
            self.fill_table()
            self.window.info_dialog(title='Сообщение:', message=response)
        except AttributeError:
            self.window.info_dialog('Сообщение:', 'Выберите слово')

    def update_handler(self, widget: Widget) -> None:
        """Update word handler."""
        try:
            self.fill_update_word_input()
            self.app.to_update_word_box()
        except AttributeError:
            self.window.info_dialog('Сообщение:', 'Выберите слово')

    def next_words_handler(self, widget: Widget) -> None:
        """Get next word list by pagination."""
        if self.next_pagination_url:
            self.fill_table(self.next_pagination_url)

    def previous_words_handler(self, widget: Widget) -> None:
        """Get next word list by pagination."""
        if self.previous_pagination_url:
            self.fill_table(self.previous_pagination_url)

    ####################################################################
    def fill_table(self, url: str | None = None) -> None:
        """Fill the Word Table box."""
        words_response = send_get_request(WORDS_PATH, url)
        self.words_table.data = words_response['results']
        self.next_pagination_url = words_response['next']
        self.previous_pagination_url = words_response['previous']

    def fill_update_word_input(self) -> None:
        """Fill the word update input fields."""
        # Get word data.
        word_data = self.words_table.selection
        # Fill update word box.
        update_word_box = self.app.update_word_box
        update_word_box.word_pk = word_data.pk
        update_word_box.eng_word_input.value = word_data.eng_word
        update_word_box.rus_word_input.value = word_data.rus_word


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
