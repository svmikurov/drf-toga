"""Task abstract base class module."""

import abc


class TaskABC(abc.ABC):
    """Task abstract base class."""

    @abc.abstractmethod
    def create_new_task(self) -> dict[str, str]:
        """Create new task."""
        raise NotImplementedError
