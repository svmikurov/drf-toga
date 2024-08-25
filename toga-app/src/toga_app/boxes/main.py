"""Application Main Box."""

from toga_app.boxes.base import BaseBox
from toga_app.boxes.styled import BoxHeading
from toga_app.move_btns import BoxButtons


class MainBox(BaseBox):
    """Class representing the main box of the application."""

    box_heading = BoxHeading(text='Добро пожаловать!')

    def __init__(self, move_btns: BoxButtons) -> None:
        """Construct the Main box."""
        super().__init__()
        self.move_btns = move_btns

        self.add(
            self.box_heading,
            self.move_btns.btn_move_words_box,
            self.move_btns.btn_move_create_word_box,
            self.move_btns.btn_move_explore_lsp_box,
            self.move_btns.btn_move_auth_box,
        )
