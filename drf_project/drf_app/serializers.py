"""DRF serializers module."""

from rest_framework import serializers

from drf_app.models.words import Word


class WordSerializer(serializers.ModelSerializer):
    """Word model serializer."""

    class Meta:
        """Construct response."""

        model = Word
        fields = ('eng_word', 'rus_word')
