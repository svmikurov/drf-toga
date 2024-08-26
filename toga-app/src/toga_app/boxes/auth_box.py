"""Auth box."""

import toga
from travertino.constants import COLUMN

from toga_app.contrib.http_requests import send_post_request
from toga_app.move_btns import BoxButtons

LOGIN_PATH = 'drf-auth/login/'


class AuthenticationBox(toga.Box):
    """Authentication Box."""

    def __init__(self, move_btns: BoxButtons) -> None:
        """Construct."""
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

    def login_handler(self, widget: toga.Widget) -> None:
        """Log in button handler."""
        self.login_request(
            self.username_input.value, self.password_input.value
        )  # noqa: E501

    def login_request(self, username: str, password: str) -> None:
        """Log in request."""
        response = send_post_request(
            path='auth/token/login/',
            payload={
                'username': username,
                'password': password,
            },
        )
        self.window.info_dialog('Сообщение:', str(response.json()))
