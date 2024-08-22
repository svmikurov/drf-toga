"""Mathematical calculate exercise views module."""
# ruff: noqa: I001

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.task_factory import TaskFactory


class MathCalcExerciseAPIView(APIView):
    """Mathematical calculate exercise view."""

    def post(self, request: Request, **kwargs: object) -> Response:
        """Render the task question."""
        task_params: dict = request.query_params.dict()
        task_data = TaskFactory.create_task(task_params)
        return Response(task_data)
