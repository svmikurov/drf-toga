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


class TogaApp(toga.App):
    """Simple Toga application."""

    main_box: boxes.MainBox
    words_box: boxes.BaseBox
    create_word_box: boxes.BaseBox
    move_btns: Buttons

    def __init__(self):
        super().__init__()
        self.move_btn_callbacks = {
            'main_box': self.to_main_box,
            'words_box': self.to_words_box,
            'create_word_box': self.to_create_word_box,
        }
        self.move_btns = Buttons(self.move_btn_callbacks)

    def startup(self) -> None:
        """Construct Main window consider other windows."""
        # Create Box instants.
        for instant_name, box_class in BOX_CLASSES.items():
            setattr(self, instant_name, box_class(self.move_btns))

        self.main_window = toga.MainWindow(size=MAIN_WINDOW_SIZE)
        self.main_window.content = self.main_box
        self.main_window.show()

    ####################################################################
    # Button callback functions
    def to_main_box(self):
        """Move to Main box."""
        self.set_main_window_content(self.main_box)

    def to_words_box(self):
        """Move to Words box."""
        self.set_main_window_content(self.words_box)

    def to_create_word_box(self):
        """Move to Create Word box."""
        self.set_main_window_content(self.create_word_box)
        # End Button callback functions
        ###############################

    def set_main_window_content(self, box: boxes.BaseBox):
        """Set the content of the window as the given box."""
        self.main_window.content = box


def main() -> toga.App:
    """Return Toga app."""
    return TogaApp()
