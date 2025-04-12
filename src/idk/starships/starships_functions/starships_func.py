from httpx import Client as Session
from ...schemas.handles_exception import get_handles_exception
from ...characters.characters_functions.character_name_by_id import search_character_name_by_id
from ...films.films_functions.film_func import search_film_name_by_id
from ..models.starship import Starship
from ...constants.constants import BASE_URL

def starships_list(session: Session) -> list[str]:
    """Get a list of starship names from the Star Wars API."""

    page: int = 1
    names: list[str] = []
    while page < 5:
        if (response := get_handles_exception(session, f"{BASE_URL}starships/?page={page}")) is not None:
            for starship in response.json()["results"]:
                names.append(starship["name"])
        page += 1
    return names

def pages_list(session: Session) -> list[list[str]]:
    """This function divides the list of starship names into pages of 10 names each."""
    
    names: list[str] = starships_list(session)
    pages: list[list[str]] = []
    for i in range(0, len(names), 10):
        pages.append(names[i:i + 10])
    return pages

def search_starship_by_name(session: Session, name: str) -> dict[str, str | list[str]] | None:
    """Search for a starship by name and return their details."""

    if (response := get_handles_exception(session, f"{BASE_URL}starships/?search={name}")) is not None:
        starship: dict[str, str | list[str]] = dict(Starship(**response.json()["results"][0]))
        starship["pilots"] = [str(search_character_name_by_id(session, int(pilot.split("/")[-2]))) for pilot in starship["pilots"]]
        starship["films"] = [str(search_film_name_by_id(session, int(film.split("/")[-2]))) for film in starship["films"]]
        return starship
    return None

def search_starship_name_by_id(session: Session, id: int) -> str | None:
    """Search for a starship by ID and return their name."""

    if (response := get_handles_exception(session, f"{BASE_URL}starships/{id}/")) is not None:
        return response.json()["name"]
    return None