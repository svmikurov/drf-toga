"""Learn Toga widget toolkit application."""

import toga

from toga_app.boxes.main import MainBox

class TogaApp(toga.App):
    """Simple Toga application."""

    main_box: MainBox
    main_window: toga.Window

    def startup(self) -> None:
        """Construct Main window consider other windows."""
        self.main_window = toga.MainWindow()

        self.main_box = MainBox()

        self.main_window.content = self.main_box
        self.main_window.show()


def main() -> toga.App:
    """Return Toga app."""
    return TogaApp()
