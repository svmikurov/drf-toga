"""Learn Toga widget toolkit application."""

import toga

from toga_app import boxes
from toga_app.consts import MAIN_WINDOW_SIZE
from toga_app.move_btns import BoxButtons

BOX_CLASSES = {
    'main_box': boxes.MainBox,
    'words_box': boxes.WordsBox,
    'create_word_box': boxes.CreateWordBox,
    'update_word_box': boxes.UpdateWordBox,
    'explore_lsp_box': boxes.ExploreLSPBox,
    'auth_box': boxes.AuthenticationBox,
}


class TogaApp(toga.App):
    """Main app instance."""

    main_box: boxes.MainBox
    words_box: boxes.WordsBox
    words_table: toga.Table
    create_word_box: boxes.CreateWordBox
    update_word_box: boxes.UpdateWordBox
    explore_lsp_box: boxes.ExploreLSPBox
    auth_box: boxes.AuthenticationBox
    move_btns: BoxButtons

    def __init__(self) -> None:
        """Construct the Main Box window."""
        super().__init__()
        self.move_btn_callbacks = {
            'main_box': self.to_main_box,
            'words_box': self.to_words_box,
            'create_word_box': self.to_create_word_box,
            'update_word_box': self.to_update_word_box,
            'explore_lsp_box': self.to_explore_lsp_box,
            'auth_box': self.to_auth_box,
        }
        self.move_btns = BoxButtons(self.move_btn_callbacks)
        # Create Box instants.
        for instant_name, box_class in BOX_CLASSES.items():
            setattr(self, instant_name, box_class(self.move_btns))

    def startup(self) -> None:
        """Construct Main window consider other windows."""
        self.main_window = toga.MainWindow(size=MAIN_WINDOW_SIZE)
        self.main_window.content = self.main_box
        self.main_window.show()

    ####################################################################
    # Move button callback functions
    def to_main_box(self) -> None:
        """Move to Main box."""
        self.set_main_window_content(self.main_box)

    def to_words_box(self) -> None:
        """Move to Words box."""
        self.set_main_window_content(self.words_box)
        self.words_box.fill_table()

    def to_create_word_box(self) -> None:
        """Move to Create Word box."""
        self.set_main_window_content(self.create_word_box)

    def to_update_word_box(self) -> None:
        """Move to Update Word box."""
        self.set_main_window_content(self.update_word_box)
        self.fill_word_update_input()

    def to_explore_lsp_box(self) -> None:
        """Move to Explore LSP box."""
        self.set_main_window_content(self.explore_lsp_box)

    def to_auth_box(self) -> None:
        """Move to Auth Box."""
        self.set_main_window_content(self.auth_box)

    ####################################################################
    # Functions for managing instances of other classes.
    def set_main_window_content(self, box: boxes.BaseBox) -> None:
        """Set the content of the window as the given box."""
        self.main_window.content = box

    def fill_word_update_input(self) -> None:
        """Fill the word update input fields."""
        # Get word data.
        word_data = self.words_box.words_table.selection
        # Apply word data.
        self.update_word_box.word_pk = word_data.pk
        self.update_word_box.eng_word_input.value = word_data.eng_word
        self.update_word_box.rus_word_input.value = word_data.rus_word

def main() -> toga.App:
    """Return Toga app."""
    return TogaApp()
