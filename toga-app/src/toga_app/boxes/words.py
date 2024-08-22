from toga_app.boxes.base import BaseBox
from toga_app.boxes.components.labels import BoxHeading
from toga_app.move_btns import Buttons


class WordsBox(Buttons, BaseBox):

    box_heading = BoxHeading(
        text='Англо-Русский словарь',
    )

    def __init__(self, move_btn_callbacks: dict) -> None:
        super().__init__()
        self.move_btn_callbacks = move_btn_callbacks

        self.add(
            self.box_heading,
            self.btn_move_main_box,
        )
