"""Learn DRF views module."""

from rest_framework import generics

from drf_app.models.words import Word
from drf_app.serializers import WordSerializer


class WordListCreateAPIView(generics.ListCreateAPIView):
    """Word List API view."""

    queryset = Word.objects.all()
    serializer_class = WordSerializer


class DeleteWordAPIView(generics.DestroyAPIView):
    """Delete Word API view."""

    queryset = Word.objects.all()
    serializer_class = WordSerializer
