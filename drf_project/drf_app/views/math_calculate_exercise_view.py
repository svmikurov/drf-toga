"""Mathematical calculate exercise views module."""

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from tasks.math_calculate_exercise import CalculationExercise

CALCULATION_TYPE = 'mul'
"""Alias representation of mathematical operators (`str`).
"""
MIN_VALUE = 1
"""Minimum operand value of mathematical task (`int`).
"""
MAX_VALUE = 9
"""Maximum operand value of mathematical task (`int`).
"""


class MathCalculateExerciseAPIView(APIView):
    """Mathematical calculate exercise view."""

    def get(self, request: Request) -> Response:
        """Render the task.

        :param request: Request parameters.
        :return: The rendered data.
        """
        task = CalculationExercise(
            calculation_type=CALCULATION_TYPE,
            min_value=MIN_VALUE,
            max_value=MAX_VALUE,
        )
        task_data = {
            'question': task.question_text,
        }

        return Response(task_data)
