"""English-Russian dictionary modul."""

from django.db import models


class Word(models.Model):
    """English-Russian dictionary."""

    eng_word = models.CharField(max_length=75)
    rus_word = models.CharField(max_length=75)

    def __str__(self) -> str:
        """Represent the word instance."""
        return f'{self.eng_word} - {self.rus_word}'
