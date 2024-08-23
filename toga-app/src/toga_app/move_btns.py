import toga
from toga import MainWindow

from toga_app.boxes import BaseBox
from toga_app.boxes.styled import StyledButton

class Buttons:

    move_btn_callbacks: dict

    def __init__(self, main_window: MainWindow):
        self.main_window = main_window
        self.added_buttons = dict()

    def add_btn_to(self, box_name, move_btn_names):
        btn = toga.Button(
            text=move_btn_names[box_name],
            on_press=lambda _: self.set_main_window_content(box_name)
        )
        setattr(self, box_name, btn)
        self.added_buttons.update({box_name: getattr(self, box_name)})

    def get_btn_to(self, box_name):
        return self.added_buttons.get(box_name)

    def move_btns(self):
        pass

    def btn_move_create_word_box(self):
        return StyledButton(
        'Добавить слово',
        on_press=lambda _: self.move_btn_callbacks['create_word_box'](),
    )

    def set_main_window_content(self, box_name: BaseBox):
        """Set the content of the window as the given box."""
        self.main_window.content = box_name