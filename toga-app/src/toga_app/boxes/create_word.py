import toga

from toga_app.boxes.base import BaseBox

from toga_app.boxes.styled import StyledTextInput, StyledButton, BoxHeading

HOST_API = 'http://127.0.0.1:8000/api/v1/'
URL_PATH = 'words/list/'


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
            self.move_btns.btn_move_main_box,
            self.move_btns.btn_move_words_box,
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
