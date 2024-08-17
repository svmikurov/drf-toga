"""My first application."""

import httpx
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


def greeting(name):
    if name:
        return f"Hello, from {name}!"
    else:
        return "Hello, from Toga!"


class TogaApp(toga.App):

    def startup(self):
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

    def say_hello(self, widget):
        """Get response from drf_project."""
        with httpx.Client() as client:
            response = client.get('http://127.0.0.1:8000/api/v1/hello')

        if response.status_code == 200:
            payload = response.json()
        else:
            payload = dict()

        self.main_window.info_dialog(
            title='Greeting',
            message=greeting(payload.get('body')),
        )


def main():
    return TogaApp()
