"""Application Main Box"""

from toga_app.boxes.base import BaseBox
from toga_app.boxes.styled import BoxHeading
from toga_app.move_btns import Buttons


class MainBox(BaseBox):
    """Class representing the main box of the application."""

    box_heading = BoxHeading(text='Добро пожаловать в приложение!')

    def __init__(self, move_btns: dict[str, Buttons]) -> None:
        """Construct Main box"""
        super().__init__()
        self.move_btns = move_btns

        self.add(
            self.box_heading,
            self.move_btns.get_btn_to('words_box'),
            self.move_btns.get_btn_to('create_word_box'),
        )
