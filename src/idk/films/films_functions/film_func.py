from httpx import Client as Session
from ...schemas.handles_exception import get_handles_exception
from ..models.films import Films
from ...constants.constants import BASE_URL


def search_film_name_by_id(session: Session, id: int) -> str | None:
    """Search for a film by ID and return its name."""

    if (response := get_handles_exception(session, f"{BASE_URL}films/{id}/")) is not None:
        return response.json()["title"]
    return None

def films_pages_list(session: Session) -> list[str]:
    """Get a list of film titles from the Star Wars API."""
    
    page: int = 1
    titles: list[str] = []
    while page < 7:
        if (response := search_film_name_by_id(session, page)) is not None:
            titles.append(response)
        page += 1
    return titles

def search_film_by_title(session: Session, title: str) -> dict[str, str | list[str]] | None:
    """Search for a film by title and return its details."""

    if (response := get_handles_exception(session, f"{BASE_URL}films/?search={title}")) is not None:
        film: dict[str, str | list[str]] = dict(Films(**response.json()["results"][0]))
        return film
    return None