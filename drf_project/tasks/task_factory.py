"""Create task factory method."""

from tasks.math_calculate_exercise import CalculationExercise

MIN_VALUE = 1
"""Minimum operand value of mathematical task (`int`).
"""
MAX_VALUE = 9
"""Maximum operand value of mathematical task (`int`).
"""


class TaskFactory:
    """Create task."""

    task_classes = {
        'mul': CalculationExercise('mul', MIN_VALUE, MAX_VALUE),
    }

    @staticmethod
    def create_task(task_type: str) -> dict[str, str]:
        """Create task and return question text.

        :param task_type: Task name type (`str`).
        :return task_data: Task data to render for user
        (`dict[str, str]`).
        """
        task = TaskFactory.task_classes[task_type]
        task_data = task.create_new_task()
        return task_data
