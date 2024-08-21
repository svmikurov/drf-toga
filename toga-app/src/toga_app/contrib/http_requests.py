"""Requests module."""

import httpx


def get_http_response(url: str) -> object:
    """Get http response."""
    with httpx.Client() as client:
        response = client.get(url=url)
    payload = response.json()
    return payload
