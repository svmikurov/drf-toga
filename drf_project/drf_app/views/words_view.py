"""English-Russian word views module."""

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class WordListAPIView(APIView):
    """English-Russian word list views."""

    def get(self, request: Request) -> Response:
        """Render English-Russian word list."""
        return Response(
            {
                'black': 'черный',
                'blue': 'синий',
            }
        )
