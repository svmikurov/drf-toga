"""Learn Toga widget toolkit application."""

import toga
from toga import Widget


class BaseWindow(toga.App):
    """Base window representation with MainWindow class.

    Inherit this class to create the new window representations.
    """

    formal_name = 'Формальное имя'
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
        self.word_list_box.add(self.btn_switch_main_window)
        super().startup()

    def switch_word_list_window(self, widget: Widget) -> None:
        """Switch to Word List window."""
        self.main_window.content = self.word_list_box

    @property
    def btn_switch_word_list_window(self) -> toga.Button:
        """Button to switch to the Word List window."""
        return toga.Button(
            text='Англо-Русский словарь',
            on_press=self.switch_word_list_window,
        )


class MathematicalWindow(BaseWindow):
    """Mathematical window representation."""

    math_box = toga.Box()

    def startup(self) -> None:
        """Construct the Mathematical window representation."""
        self.math_box.add(self.btn_switch_main_window)
        super().startup()

    def switch_math_window(self, widget: Widget) -> None:
        """Switch to Mathematical window."""
        self.main_window.content = self.math_box

    @property
    def btn_switch_math_window(self) -> toga.Button:
        """Button to switch to the Mathematical window."""
        return toga.Button(
            text='Математические вычисления',
            on_press=self.switch_math_window,
        )

class TogaApp(
    WordListWindow,
    MathematicalWindow,
):
    """Simple Toga application."""
    def startup(self) -> None:
        """Construct Main window."""
        self.main_box.add(self.btn_switch_word_list_window)
        self.main_box.add(self.btn_switch_math_window)
        super().startup()


def main() -> toga.App:
    """Return Toga app."""
    return TogaApp()
