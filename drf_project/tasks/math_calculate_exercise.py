"""The mathematical calculate exercise module."""

import operator
from random import randint

MATH_CALCULATION_TYPE = (
    ('add', 'Сложение'),
    ('sub', 'Вычитание'),
    ('mul', 'Умножение'),
)
"""Mathematical exercise type choice.

Use in choices, note: max_length=10.
"""


class CalculationExercise:
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
    """Еhe text representation of a mathematical expression to render to
    the user (None | `str`).
    """
    answer_text = None
    """The text representation of the result of calculating
    a mathematical expression (None | `str`).
    """

    def __init__(
        self,
        *,
        calculation_type: str,
        min_value: int,
        max_value: int,
    ) -> None:
        """Construct calculation exercise."""
        self.calculation_type = calculation_type
        self.min_value = min_value
        self.max_value = max_value
        self.__call__()

    def __call__(self) -> None:
        """Create task."""
        self._set_task_solution(
            self.calculation_type,
            self.min_value,
            self.max_value,
        )

    def _set_task_solution(  # noqa: D417
        self,
        calculation_type: str,
        min_value: int,
        max_value: int,
    ) -> None:
        """Create and set question text with answer text.

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
