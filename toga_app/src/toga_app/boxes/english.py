"""English-Russian dictionary boxes module."""

import typing
from urllib.parse import urljoin

import httpx
import toga

API_HOST = 'http://127.0.0.1:8000/api/v1/'
WORD_LIST_PATH = 'words/list/'


def get_word_list(url: str) -> typing.Any:  # noqa: ANN401
    """Get word list from host.

    :param url: Word list request url.
    :return payload: Json word list.
    """
    with httpx.Client() as client:
        response = client.get(url)
    payload = response.json()
    return payload


add_box = toga.Box
"""Add a word to the English-Russian dictionary box (`Box`).
"""

word_list = toga.DetailedList(
    data=get_word_list(url=urljoin(API_HOST, WORD_LIST_PATH))
)

list_box = toga.Box(children=[])
"""View English-Russian dictionary words (`Box`).
"""
