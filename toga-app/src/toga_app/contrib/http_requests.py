"""Requests module."""

import httpx
from httpx import Request, Response

IS_AUTH = 1


class JWTAuth(httpx.Auth):
    """Create custom auth."""

    requires_response_body = True

    def __init__(
        self,
        access_token: object,
        refresh_token: object,
        refresh_url: object,
    ) -> None:
        """Construct auth."""
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.refresh_url = refresh_url

    def auth_flow(self, request: Request) -> None:
        """Auth."""
        request.headers['X-Authentication'] = self.access_token
        response = yield request

        if response.status_code == 401:
            # If the server issues a 401 response, then issue a request
            # to refresh tokens, and resend the request.
            refresh_response = yield self.build_refresh_request()
            self.update_tokens(refresh_response)

            request.headers['X-Authentication'] = self.access_token
            yield request

    def build_refresh_request(self) -> None:
        """Build refresh request."""
        # Return an `httpx.Request` for refreshing tokens.
        ...

    def update_tokens(self, response: Response) -> None:
        """Update tokens."""
        # Update the `.access_token` and `.refresh_token` tokens
        # based on a refresh response.
        data = response.json()  # noqa: F841
        ...


auth = httpx.BasicAuth('admin', '1q2s3d4r') if IS_AUTH else None

access_token = ...
refresh_token = ...
refresh_url = ...

custom_auth = JWTAuth(access_token, refresh_token, refresh_url)


def send_get_request(url: str) -> list[dict]:
    """Send a `GET` request."""
    with httpx.Client(auth=auth) as client:
        response = client.get(url=url)
    return response.json()


def send_post_request(url: str, data: dict) -> str:
    """Send a `POST` request."""
    with httpx.Client(auth=auth) as client:
        response = client.post(url, json=data)
    return str(response.json())


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
