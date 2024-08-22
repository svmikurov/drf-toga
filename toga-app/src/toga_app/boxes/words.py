
import toga
from toga.style import Pack
from travertino.constants import COLUMN

from toga_app.boxes.base import BaseBox
from toga_app.boxes.components.line import LineBox


class WordsBox(BaseBox):

    def __init__(self, move_buttons: dict) -> None:
        super().__init__()
        self.move_buttons = move_buttons
        self.style = Pack(flex=1, direction=COLUMN)

        box_label = LineBox(
            children=[
                toga.Label('Англо-Русский словарь'),
            ]
        )
        move_main_box_btn = toga.Button(
            'На главную',
            on_press=lambda _: self.move_buttons['main_box'](),
        )

        self.add(box_label, move_main_box_btn)
