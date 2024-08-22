"""Requests module."""

import httpx


def get_http_response(url: str) -> list[dict]:
    """Get http response."""
    with httpx.Client() as client:
        response = client.get(url=url)
    payload = response.json()
    return payload


def send_post_request(url: str, data: dict) -> str:
    """Send a `POST` request."""
    response = httpx.post(url, json=data)
    response.close()
    return str(response.json())

def send_delete_request(url: str) -> str:
    """Send a `DELETE` request."""
    response = httpx.delete(url)
    response.close()
    return str(response)
