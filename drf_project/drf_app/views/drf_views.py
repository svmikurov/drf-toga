"""Django REST framework views."""

from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from drf_app.models.words import Word
from drf_app.serializers import WordSerializer

IS_PERMISSION = 1


class WordListCreateAPIView(generics.ListCreateAPIView):
    """Word List or Create view."""

    queryset = Word.objects.all()
    serializer_class = WordSerializer
    if IS_PERMISSION:
        permission_classes = (IsAuthenticated,)


class WordRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Word Update or Delete view."""

    queryset = Word.objects.all()
    serializer_class = WordSerializer
    if IS_PERMISSION:
        permission_classes = (IsAuthenticated,)
