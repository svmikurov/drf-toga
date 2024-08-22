"""DRF serializers module."""

from rest_framework import serializers

from drf_app.models.words import Word


class WordSerializer(serializers.ModelSerializer):
    """Word model serializer."""

    class Meta:
        """Serializer configure."""

        model = Word
        fields = ('pk', 'eng_word', 'rus_word')
