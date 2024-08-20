"""Create task factory module."""

from tasks.math_calculate_exercise import CalculationExercise


class TaskFactory:
    """Create task."""

    exercise_classes = {
        'math': CalculationExercise,
    }

    @staticmethod
    def create_task(exercise_params: dict[str, str]) -> dict[str, str]:
        """Create task and return question text.

        :param exercise_params: Exercise parameters (`dict[str, str]`).
        :return task_data: Task data to render for user
        (`dict[str, str]`).
        """
        exercise_type = exercise_params.pop('exercise_type')
        task = TaskFactory.exercise_classes[exercise_type](**exercise_params)
        task_data = task.create_new_task()
        return task_data
