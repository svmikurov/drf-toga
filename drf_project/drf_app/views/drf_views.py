"""Django REST framework views."""

from contrib.generics import BaseUpdateDeleteAPIView
from rest_framework import generics

from drf_app.models.words import Word
from drf_app.serializers import WordSerializer


class WordListCreateAPIView(generics.ListCreateAPIView):
    """Word List or Create view."""

    queryset = Word.objects.all()
    serializer_class = WordSerializer


class UpdateDeleteAPIView(BaseUpdateDeleteAPIView):
    """Word Update or Delete view."""

    queryset = Word.objects.all()
    serializer_class = WordSerializer
