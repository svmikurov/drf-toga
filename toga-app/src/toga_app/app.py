"""Learn Toga widget toolkit application."""

import toga

from toga_app import boxes
from toga_app.consts import MAIN_WINDOW_SIZE


class TogaApp(toga.App):
    """Simple Toga application."""

    main_box: boxes.MainBox
    words_box: boxes.BaseBox
    create_word_box: boxes.BaseBox
    main_window: toga.Window

    BOX_CLASSES = {
        'main_box': boxes.MainBox,
        'words_box': boxes.WordsBox,
        'create_word_box': boxes.CreateWordBox,
    }

    def startup(self) -> None:
        """Construct Main window consider other windows."""
        move_btn_callbacks = {
            'main_box': self.on_main,
            'words_box': self.on_words,
            'create_word_box': self.on_create_word_box,
        }

        # Create Box instants.
        for instant_name, box_class in self.BOX_CLASSES.items():
            setattr(self, instant_name, box_class(move_btn_callbacks))

        self.main_window = toga.MainWindow(size=MAIN_WINDOW_SIZE)
        self.main_window.content = self.main_box
        self.main_window.show()

    ####################################################################
    # Button callback functions
    def on_main(self):
        """Move to Main box."""
        self.set_main_window_content(self.main_box)

    def on_words(self):
        """Move to Words box."""
        self.set_main_window_content(self.words_box)

    def on_create_word_box(self):
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
