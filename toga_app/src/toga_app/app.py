"""Learn Toga widget toolkit application."""

import toga
from toga import Widget


class BaseWindow(toga.App):
    """Base window representation with MainWindow class.

    Inherit this class to create the new window representations.
    """

    main_box = toga.Box()

    def startup(self) -> None:
        """Construct and show the Main window."""
        self.main_window = toga.MainWindow(title='Название приложения')
        self.main_window.content = self.main_box
        self.main_window.show()

    def switch_main_window(self, widget: Widget) -> None:
        """Switch to Main window."""
        self.main_window.content = self.main_box

    @property
    def btn_switch_main_window(self) -> toga.Button:
        """Button to switch to the Main window."""
        return toga.Button(
            text='Главное окно',
            on_press=self.switch_main_window,
        )


class WordListWindow(BaseWindow):
    """Word List window representation."""

    word_list_box = toga.Box()

    def startup(self) -> None:
        """Construct the Word List window."""
        # Main window contain a switch button to this window.
        self.main_box.add(self.btn_switch_word_list_window)
        # This window contain a switch button to Main window.
        self.word_list_box.add(self.btn_switch_main_window)

        super().startup()

    def switch_word_list_window(self, widget: Widget) -> None:
        """Switch to word list window."""
        self.main_window.content = self.word_list_box

    @property
    def btn_switch_word_list_window(self) -> toga.Button:
        """Button to switch to the word list window."""
        return toga.Button(
            text='Англо-Русский словарь',
            on_press=self.switch_word_list_window,
        )


class TogaApp(
    WordListWindow,
):
    """Simple Toga application."""


def main() -> toga.App:
    """Return Toga app."""
    return TogaApp()
