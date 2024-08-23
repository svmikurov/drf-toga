"""Learn Toga widget toolkit application."""

import toga

from toga_app import boxes
from toga_app.consts import MAIN_WINDOW_SIZE
from toga_app.move_btns import Buttons

BOX_CLASSES = {
    'main_box': boxes.MainBox,
    'words_box': boxes.WordsBox,
    'create_word_box': boxes.CreateWordBox,
}
MOVE_BTN_NAMES = {
    'main_box': 'На главную',
    'words_box': 'Словарь',
    'create_word_box': 'Добавить слово',
}

class TogaApp(toga.App):
    """Simple Toga application."""

    main_box: boxes.BaseBox
    move_btn: Buttons

    def startup(self) -> None:
        """Construct Main window consider other windows."""
        self.main_window = toga.MainWindow(size=MAIN_WINDOW_SIZE)

        self.move_btn = Buttons(self.main_window)
        for box_name, box_class in BOX_CLASSES.items():
            self.create_box(box_name, box_class)

        self.main_window.content = self.main_box
        self.main_window.show()

    def create_box(self, box_name, box_class):
        setattr(self, box_name, box_class(self.move_btn))
        if box_name in MOVE_BTN_NAMES:
            self.move_btn.add_btn_to(box_name, MOVE_BTN_NAMES)




def main() -> toga.App:
    """Return Toga app."""
    return TogaApp()
