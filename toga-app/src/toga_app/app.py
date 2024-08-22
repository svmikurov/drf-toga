"""Learn Toga widget toolkit application."""

import toga
from toga.style import Pack

from toga_app.boxes.base import BaseBox
from toga_app.boxes.main import MainBox
from toga_app.boxes.words import WordsBox


# class BoxFactory:
#
#     box_classes = {
#         'main_box': MainBox,
#         'words_box': WordsBox,
#     }
#
#     @classmethod
#     def create_box(cls, box_class):
#         if box_class in cls.box_classes:
#             return cls.box_classes[box_class]()


class TogaApp(toga.App):
    """Simple Toga application."""

    main_box: MainBox
    words_box: BaseBox
    main_window: toga.Window
    move_buttons: dict

    btn_style = Pack()

    def startup(self) -> None:
        """Construct Main window consider other windows."""
        box_classes = {
            'main_box': MainBox,
            'words_box': WordsBox,
        }
        move_buttons = {
            'main_box': self.on_main,
            'words_box': self.on_words,
        }
        # Create Box instants.
        for key, value in box_classes.items():
            setattr(self, key, value(move_buttons))

        self.main_window = toga.MainWindow()
        self.main_window.content = self.main_box
        self.main_window.show()

    def on_main(self):
        """Move to main box."""
        self.set_main_window_content(self.main_box)

    def on_words(self):
        """Move to welcome box."""
        self.set_main_window_content(self.words_box)

    def set_main_window_content(self, box: BaseBox):
        """Set the content of the window as the given box."""
        self.main_window.content = box

    def apply_method(self, box_instance):
        return lambda: self.set_main_window_content(box_instance)

def main() -> toga.App:
    """Return Toga app."""
    return TogaApp()
