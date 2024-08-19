"""Mathematical calculate exercise views module."""
# ruff: noqa: I001

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.task_factory import TaskFactory

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
        """Render the task question."""
        task_data = TaskFactory.create_task('mul')
        return Response(task_data)
