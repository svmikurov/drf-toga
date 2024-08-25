from urllib.parse import urljoin

import httpx
import toga
from travertino.constants import COLUMN

from toga_app.move_btns import BoxButtons

HOST_API = 'http://127.0.0.1:8000/api/v1/'
LOGIN_PATH = 'drf-auth/login/'


class AuthenticationBox(toga.Box):
    """Authentication Box."""

    def __init__(self, move_btns: BoxButtons) -> None:
        super().__init__()
        self.move_btns = move_btns
        self.username_input = toga.TextInput(placeholder='Введите имя')
        self.password_input = toga.PasswordInput(placeholder='Введите пароль')
        self.submit = toga.Button(text='Войти', on_press=self.login_handler)

        self.style.update(direction=COLUMN)

        self.add(
            self.move_btns.btn_move_main_box,
            self.username_input,
            self.password_input,
            self.submit,
        )

    def login_handler(self, widget: toga.Widget):
        """Log in button handler."""
        self.login_request(self.username_input.value, self.password_input.value)  # noqa: E501

    def login_request(self, username: str, password: str) -> None:
        """Log in request."""
        pass

        # self.username_input.clear()
        # self.password_input.clear()
