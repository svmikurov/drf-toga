"""English-Russian word views module."""

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_app.models.words import Word


class WordListAPIView(APIView):
    """English-Russian word list views."""

    def get(self, request: Request) -> Response:
        """Render English-Russian word list."""
        words = Word.objects.all()
        return Response(words.values())
