"""Requests module."""

import httpx


def send_get_request(url: str) -> list[dict]:
    """Send a `GET` request."""
    with httpx.Client() as client:
        response = client.get(url=url)
    return response.json()


def send_post_request(url: str, data: dict) -> str:
    """Send a `POST` request."""
    with httpx.Client() as client:
        response = client.post(url, json=data)
    return str(response.json())

def send_delete_request(url: str) -> str:
    """Send a `DELETE` request."""
    with httpx.Client() as client:
        response = client.delete(url)
    return str(response)
