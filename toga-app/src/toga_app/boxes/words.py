from toga_app.boxes.base import BaseBox
from toga_app.boxes.styled import BoxHeading


class WordsBox(BaseBox):

    box_heading = BoxHeading(text='Англо-Русский словарь')

    def __init__(self, move_btns) -> None:
        super().__init__()
        self.move_btns = move_btns

        self.add(
            self.box_heading,
            self.move_btns.btn_move_main_box,
        )
