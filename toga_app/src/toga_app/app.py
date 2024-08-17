"""My first application."""

import httpx
import toga
from toga.style import Pack


class TogaApp(toga.App):
    """Simple Toga application."""

    def startup(self) -> None:
        """Construct and show the Toga application."""
        main_box = toga.Box()

        button = toga.Button(
            text='Greeting',
            style=Pack(padding=(0, 5)),
            on_press=self.say_hello,
        )

        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget: object) -> None:
        """Get response from drf_project."""
        with httpx.Client() as client:
            response = client.get('http://127.0.0.1:8000/api/v1/hello')

        payload = response.json()

        self.main_window.info_dialog(
            title='Greeting',
            message=payload.get('greeting'),
        )


def main() -> toga.App:
    """Return Toga app."""
    return TogaApp()
