"""My first application."""

import httpx
import toga
from toga.style import Pack
from toga.widgets.base import Widget

MIN_VALUE = 1
"""Minimum operand value of mathematical task (`int`).
"""
MAX_VALUE = 9
"""Maximum operand value of mathematical task (`int`).
"""


class TogaApp(toga.App):
    """Simple Toga application."""

    main_box = None
    math_calc_exercise_box = None

    def startup(self) -> None:
        """Construct and show the Toga application."""
        ################################################################
        # Buttons
        btn_style = Pack(padding=(0, 2))
        btn_greeting_button = toga.Button(
            text='Greeting',
            on_press=self.say_hello,
            style=btn_style,
        )
        btn_task_button = toga.Button(
            text='Task',
            on_press=self.do_exercise,
            style=btn_style,
        )
        btn_goto_math_calc_exercise = toga.Button(
            text='Таблица умножения',
            on_press=self.goto_math_calc_exercise,
            style=btn_style,
        )
        btn_goto_back = toga.Button(
            text='Go back',
            on_press=self.do_prev_content,
            style=btn_style,
        )
        # End Buttons
        #############

        ################################################################
        # Boxes
        self.main_box = toga.Box(
            children=[
                btn_greeting_button,
                btn_goto_math_calc_exercise,
            ]
        )
        self.math_calc_exercise_box = toga.Box(
            children=[
                btn_task_button,
                btn_goto_back,
            ],
        )
        # End Boxes
        ###########

        ################################################################
        # Window
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()
        # End Window
        ############

    ####################################################################
    # Methods
    def say_hello(self, widget: Widget) -> None:
        """Get response from drf_project."""
        with httpx.Client() as client:
            response = client.get('http://127.0.0.1:8000/api/v1/hello')

        payload = response.json()

        self.main_window.info_dialog(
            title='Greeting',
            message=payload.get('greeting'),
        )

    def do_exercise(self, widget: Widget) -> None:
        """Start exercise."""
        with httpx.Client() as client:
            response = client.post(
                'http://127.0.0.1:8000/api/v1/math-calc-exercise/',
                params={
                    'task_type': 'math',
                    'calculation_type': 'mul',
                    'min_value': 1,
                    'max_value': 9,
                },
            )

        if response.status_code == 404:
            self.main_window.info_dialog(
                title='Request',
                message='Page not found',
            )
            return

        payload = response.json()
        self.main_window.info_dialog(
            title='Task:',
            message=payload.get('question'),
        )

    def goto_math_calc_exercise(self, widget: Widget) -> None:
        """Go to math calc exercise window."""
        self.main_window.content = self.math_calc_exercise_box

    def do_prev_content(self, widget: Widget) -> None:
        """Set into window content the main box."""
        self.main_window.content = self.main_box

    # End Methods
    #############


def main() -> toga.App:
    """Return Toga app."""
    return TogaApp()
