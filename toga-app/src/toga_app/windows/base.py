"""Base window representation module."""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN


class BaseWindow:
    """Base window representation with MainWindow class.

    Inherit this class to create the new window representations.
    """

    formal_name = 'Формальное имя'

    main_style: Pack
    main_box: toga.Box
    main_window: toga.MainWindow

    def startup(self) -> None:
        """Construct and show the Main window."""
        self.main_style = Pack(direction=COLUMN)
        self.main_window = toga.MainWindow(title='Название приложения')

    def goto_main_window(self, widget: toga.Widget) -> None:
        """Switch to Main window."""
        self.main_window.content = self.main_box

    @property
    def btn_goto_main_window(self) -> toga.Button:
        """Button to switch to Main window (read-only)."""
        return toga.Button(
            text='Главное окно',
            on_press=self.goto_main_window,
        )
