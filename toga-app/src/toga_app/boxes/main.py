"""Application Main Box"""

from toga_app.boxes.base import BaseBox
from toga_app.boxes.components.labels import BoxHeading
from toga_app.move_btns import Buttons


class MainBox(Buttons, BaseBox):
    """Class representing the main box of the application."""

    box_heading = BoxHeading(
        text='Добро пожаловать в приложение!',
    )

    def __init__(self, move_btn_callbacks: dict) -> None:
        """Construct Main box"""
        super().__init__()
        self.move_btn_callbacks = move_btn_callbacks

        self.add(
            self.box_heading,
            self.btn_move_words_box,
            self.btn_move_create_word_box,
        )
