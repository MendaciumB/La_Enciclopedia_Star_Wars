from httpx import Client as Session
from ...schemas.handles_exception import get_handles_exception
from ..models.films import Films
from ...constants.constants import BASE_URL



def films_list(session: Session) -> list[str] | None:
    """Get a list of film titles from the Star Wars API."""
    
    if (response := get_handles_exception(session, f"{BASE_URL}films/")) is not None:
        result = response.json()["results"]
        films: list[str] = []
        for index in range(len(result)):
            films.append(result[index]["title"])
        return films
    return None

def search_film_by_title(session: Session, title: str) -> dict[str, str | list[str]] | None:
    """Search for a film by title and return its details."""

    if (response := get_handles_exception(session, f"{BASE_URL}films/?search={title}")) is not None:
        film: dict[str, str | list[str]] = dict(Films(**response.json()["results"][0]))
        return film
    return None