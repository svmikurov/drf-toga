"""Application Main Box"""

import toga
from docutils.parsers.rst.directives.tables import align
from pygments.lexers import find_lexer_class
from toga.style import Pack
from travertino.constants import COLUMN, ROW

from toga_app.boxes.base import BaseBox
from toga_app.boxes.components.line import LineBox


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
                toga.Label(
                    style=Pack(padding=(7, 7, 7, 7)),
                    text='Добро пожаловать в приложение!'
                ),
                toga.Button(
                    'Англо-Русский словарь',
                    on_press=lambda _: self.move_buttons['words_box'](),
                )
            ],
        )
