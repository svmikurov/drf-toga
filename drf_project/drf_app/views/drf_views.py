"""Learn DRF views module."""

from rest_framework import generics

from drf_app.models.words import Word
from drf_app.serializers import WordSerializer


class WordListAPIView(generics.ListAPIView):
    """Word List API view."""

    queryset = Word.objects.all()
    serializer_class = WordSerializer
