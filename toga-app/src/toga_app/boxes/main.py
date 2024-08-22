"""Application Main Box"""

import toga
from toga.style import Pack
from travertino.constants import COLUMN

from toga_app.boxes.base import BaseBox


class MainBox(BaseBox):
    """Class representing the main box of the application."""

    def __init__(self, move_buttons) -> None:
        """Construct Main box"""
        super().__init__()
        self.move_buttons = move_buttons
        main_box = self.build_main_box()
        self.add(main_box)

    def build_main_box(self):
        return BaseBox(
            style=Pack(flex=1, direction=COLUMN),
            children=[
                toga.Label(text='Добро пожаловать в приложение!'),
                toga.Button(
                    'Англо-Русский словарь',
                    on_press=lambda _: self.move_buttons['words_box'](),
                )
            ],
        )
