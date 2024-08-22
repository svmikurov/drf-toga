"""Application Main Box"""

from tkinter import CENTER

import toga
from toga.style import Pack
from travertino.constants import COLUMN, ROW, RIGHT

from toga_app.boxes.base import BaseBox


class MainBox(BaseBox):
    """Class representing the main box of the application."""

    def __init__(self) -> None:
        """construct Main box"""
        super().__init__()
        main_box = self.build_main_box()
        self.add(main_box)

    @classmethod
    def build_main_box(cls):
        return BaseBox(
            style=Pack(flex=1, direction=COLUMN),
            children=[
                BaseBox(
                    style=Pack(padding=(15, 20)),
                    children=[
                        BaseBox(style=Pack(flex=1)),
                        toga.Label(text='Добро пожаловать в приложение!'),
                        BaseBox(style=Pack(flex=1)),
                    ],
                ),
                BaseBox(
                    children=[
                        toga.Button(
                            text='Англо-Русский словарь',
                            on_press=cls.goto_word_list_window,
                            style=Pack(flex=1),
                        ),
                    ],
                ),
            ],
        )

    def goto_word_list_window(self) -> None:
        """Switch to Word List window."""
        self.fill_word_list_table()
        self.main_window.content = self.word_list_box