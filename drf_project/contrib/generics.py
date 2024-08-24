"""Project's derived view classes."""

from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response


class BaseUpdateDeleteAPIView(
    mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView
):
    """Concrete view for update or delete a model instance."""

    def put(
        self, request: Request, *args: object, **kwargs: object
    ) -> Response:
        """Update a movel instance."""
        return self.update(request, *args, **kwargs)

    def patch(
        self, request: Request, *args: object, **kwargs: object
    ) -> Response:
        """Update a movel instance."""
        return self.partial_update(request, *args, **kwargs)

    def delete(
        self, request: Request, *args: object, **kwargs: object
    ) -> Response:
        """Delete a movel instance."""
        return self.destroy(request, *args, **kwargs)
