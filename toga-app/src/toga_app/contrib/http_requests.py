"""Requests module."""

from urllib.parse import urljoin

import httpx
from httpx import Request, Response

IS_AUTH = 1
HOST_API = 'http://127.0.0.1:8000/'
GET_TOKEN_PATH = 'auth/token/login/'


class MuAuth(httpx.Auth):
    """Create custom auth."""

    _access_token = None

    def __init__(self, username: str, password: str) -> None:
        """Construct auth."""
        self.payload = {
            'username': username,
            'password': password,
        }

    def auth_flow(self, request: Request) -> Request:
        """Auth flow."""
        response = yield request
        if response.status_code == 401:
            request.headers['Authorization'] = f'Token {self.access_token}'
            yield request

    @property
    def access_token(self) -> str:
        """Access token."""
        if not self._access_token:
            self.get_access_token()
        return self._access_token

    def get_access_token(self) -> None:
        """Get access token."""
        response = send_post_request(path=GET_TOKEN_PATH, payload=self.payload)
        self._access_token = response.json()['auth_token']


auth = MuAuth('admin', '1q2s3d4r') if IS_AUTH else None


def send_get_request(url: str) -> list[dict]:
    """Send a `GET` request."""
    with httpx.Client(auth=auth) as client:
        response = client.get(url=url)
    return response.json()


def send_post_request(path: str, payload: dict) -> Response:
    """Send a `POST` request."""
    with httpx.Client(auth=auth) as client:
        response = client.post(url=urljoin(HOST_API, path), json=payload)
    return response


def send_patch_request(url: str, data: dict) -> str:
    """Send a `POST` request."""
    with httpx.Client(auth=auth) as client:
        response = client.patch(url, json=data)
    return str(response.json())


def send_delete_request(url: str) -> str:
    """Send a `DELETE` request."""
    with httpx.Client(auth=auth) as client:
        response = client.delete(url)
    return str(response)
