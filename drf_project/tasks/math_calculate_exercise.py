"""The mathematical calculate exercise module."""

import operator
from random import randint

from tasks.task_abc import TaskABC

MATH_CALCULATION_TYPE = (
    ('add', 'Сложение'),
    ('sub', 'Вычитание'),
    ('mul', 'Умножение'),
)
"""Mathematical exercise type choice.
"""


class CalculationExercise(TaskABC):
    """Calculation exercise class with two operands.

    Parameters
    ----------
    calculation_type : `str`
        Alias representation of mathematical operator of task.
    min_value : `int`
        Minimum value of operands.
    max_value : `int`
        Maximum value of operands.

    """

    _OPS = {
        'add': operator.add,
        'sub': operator.sub,
        'mul': operator.mul,
    }
    """Alias representation of mathematical operators
    (`Dict[str, object]`).
    """
    _OP_SIGNS = {
        'add': '+',
        'sub': '-',
        'mul': '*',
    }
    """Alias representation of mathematical sign
    (`Dict[str, str]`).
    """
    question_text = None
    """The text representation of a mathematical expression to render to
    the user (`None` | `str`).
    """
    answer_text = None
    """The text representation of the result of calculating
    a mathematical expression (`None` | `str`).
    """

    def __init__(
        self,
        calculation_type: str,
        min_value: int | str,
        max_value: int | str,
    ) -> None:
        """Construct calculation exercise."""
        self.calculation_type = calculation_type
        self.min_value = int(min_value)
        self.max_value = int(max_value)

    def create_new_task(self) -> dict[str, str]:
        """Create new task."""
        self._set_task_solution(
            self.calculation_type,
            self.min_value,
            self.max_value,
        )
        task_data = {
            'question': self.question_text,
        }
        return task_data

    def _set_task_solution(
        self,
        calculation_type: str,
        min_value: int,
        max_value: int,
    ) -> None:
        """Create and set question text with answer text.

        This base logic to create task, for class API management use
        other attributes.

        Parameters
        ----------
        calculation_type : `str`
            Alias representation of the calculation type, can be
            'add', 'sub' or 'mul' operator.
        min_value : `int`
            Minimum operand value.
        max_value : `int`
            Maximum operand value.

        """
        first_operand = randint(min_value, max_value)
        second_operand = randint(min_value, max_value)
        math_sign = self._OP_SIGNS.get(calculation_type)

        question = f'{first_operand} {math_sign} {second_operand}'
        answer = self._OPS[calculation_type](first_operand, second_operand)

        self.question_text = question
        self.answer_text = str(answer)
