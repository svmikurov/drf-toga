"""Application Main Box"""

from toga_app.boxes.base import BaseBox
from toga_app.boxes.styled import BoxHeading


class MainBox(BaseBox):
    """Class representing the main box of the application."""

    box_heading = BoxHeading(text='Добро пожаловать в приложение!')

    def __init__(self, move_btns) -> None:
        super().__init__()
        self.move_btns = move_btns

        self.add(
            self.box_heading,
            self.move_btns.btn_move_words_box,
            self.move_btns.btn_move_create_word_box,
        )
