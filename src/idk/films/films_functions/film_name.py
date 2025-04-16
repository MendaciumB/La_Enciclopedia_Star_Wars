from httpx import Client as Session
from ...schemas.handles_exception import get_handles_exception


def search_film_name_by_url(session: Session, url: str) -> str | None:
    """Search for a film by URL and return their name."""

    if (response := get_handles_exception(session, url)) is not None:
        return response.json()["title"]
    return None
