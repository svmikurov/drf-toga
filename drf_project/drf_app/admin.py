"""Admin management of models module."""

from django.contrib import admin

from drf_app.models.words import Word


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    """Admin management of Word model."""

    list_display = ['eng_word', 'rus_word']
