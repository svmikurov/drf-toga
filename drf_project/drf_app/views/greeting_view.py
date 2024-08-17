"""Views module."""

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloAPIView(APIView):
    """Greeting view."""

    def get(self, request: Request) -> Response:
        """Return greeting."""
        return Response(
            {
                'greeting': 'Hello from DRF to Toga!',
            }
        )
