from httpx import Client as Session
from ...schemas.handles_exception import get_handles_exception
from ...characters.characters_functions.character_name_by_id import search_character_name_by_id
from ...films.films_functions.film_func import search_film_name_by_id
from ..models.planet import Planet
from ...constants.constants import BASE_URL


def planets_list(session: Session) -> list[str]:
    """Get a list of planet names from the Star Wars API."""

    page: int = 1
    names: list[str] = []
    while page < 7:
        if (response := get_handles_exception(session, f"{BASE_URL}planets/?page={page}")) is not None:
            for planet in response.json()["results"]:
                names.append(planet["name"])
        page += 1
    return names

def planets_pages_list(session: Session) -> list[list[str]]:
    """This function divides the list of planet names into pages of 10 names each."""
    
    names: list[str] = planets_list(session)
    pages: list[list[str]] = []
    for i in range(0, len(names), 10):
        pages.append(names[i:i + 10])
    return pages

def search_planet_by_name(session: Session, name: str) -> dict[str, str | list[str]] | None:
    """Search for a planet by name and return their details."""

    if (response := get_handles_exception(session, f"{BASE_URL}planets/?search={name}")) is not None:
        planet: dict[str, str | list[str]] = dict(Planet(**response.json()["results"][0]))
        planet["residents"] = [str(search_character_name_by_id(session, int(resident.split("/")[-2]))) for resident in planet["residents"]]
        planet["films"] = [str(search_film_name_by_id(session, int(film.split("/")[-2]))) for film in planet["films"]]
        return planet
    return None

def search_planet_name_by_id(session: Session, id: int) -> str | None:
    """Search for a planet by ID and return their name."""

    if (response := get_handles_exception(session, f"{BASE_URL}planets/{id}/")) is not None:
        return response.json()["name"]
    return None