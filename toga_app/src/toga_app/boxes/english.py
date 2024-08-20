"""English-Russian dictionary boxes module."""

import typing
from urllib.parse import urljoin

import httpx
import toga
from toga.style import Pack

API_HOST = 'http://127.0.0.1:8000/api/v1/'
WORD_LIST_PATH = 'words/list/'

btn_style = Pack(padding=(0, 2))


def request_translations(url: str) -> typing.Any:  # noqa: ANN401
    """Request the word translations from host.

    :param url: Word list request url.
    :return: Json word list.
    """
    with httpx.Client() as client:
        response = client.get(url)
    return response.json()


########################################################################
# Add word box
add_box = toga.Box
"""Add a word to the English-Russian dictionary box (`Box`).
"""
# End Add word box
##################


########################################################################
# Word list box
class WordListBox:
    """Word list box representation class.

    :param main_window: Main window (`MainWindow`).
    """

    def __init__(self, main_window: toga.MainWindow) -> None:
        """Add main window to construct word list box."""
        self.main_window = main_window

    # _translations = request_translations(url=urljoin(API_HOST, WORD_LIST_PATH))
    # """List of word translations (`list[dict]`).
    # """

    table = toga.Table(
        headings=['English', 'Russian'],
        data=[
            ('black', 'черный'),
            ('red', 'красный')
        ],
    )
    """Detailed list (`DetailedList`).
    """

    word_list_box = toga.Box(
        children=[table],
    )
    """View English-Russian dictionary words (`Box`).
    """

    def goto_word_list_box(self) -> None:
        """Go to current box instance at window."""
        self.main_window.content = self.word_list_box

    btn_word_list_box = toga.Button(
        text='Англо-Русский словарь',
        on_press=goto_word_list_box,
        style=btn_style,
    )
    """Button to go to current instance box (`Button`).
    """

    # End Word list box
    ###################
