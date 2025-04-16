import math
from httpx import Client as Session
from ...schemas.handles_exception import get_handles_exception
from ...characters.characters_functions.character_name import search_character_name_by_url
from ...films.films_functions.film_name import search_film_name_by_url
from ..models.planet import Planet
from ...constants.constants import BASE_URL, PAGINATION


def planets_total_pages(session: Session) -> int:
    """Get the total number of pages of planets from the Star Wars API."""
    total_pages: int = 1
    if (response := get_handles_exception(session, f"{BASE_URL}people/?page={total_pages}")) is not None:
        result = response.json()
        total_pages = math.ceil(result["count"]/PAGINATION)
    return total_pages


def planets_page_list(session: Session, page: int) -> list[str] | None:
    """Get a list of planet names of a page from the Star Wars API."""

    if (response := get_handles_exception(session, f"{BASE_URL}planets/?page={page}")) is not None:
        return [planet["name"] for planet in response.json()["results"]]
    return None


# def planets_list(session: Session) -> list[str]:
#     """Get a list of planet names from the Star Wars API."""

#     page: int = 1
#     names: list[str] = []
#     while page < 7:
#         if (response := get_handles_exception(session, f"{BASE_URL}planets/?page={page}")) is not None:
#             for planet in response.json()["results"]:
#                 names.append(planet["name"])
#         page += 1
#     return names

# def planets_pages_list(session: Session) -> list[list[str]]:
#     """This function divides the list of planet names into pages of 10 names each."""
    
#     names: list[str] = planets_list(session)
#     pages: list[list[str]] = []
#     for i in range(0, len(names), 10):
#         pages.append(names[i:i + 10])
#     return pages

def search_planet_by_name(session: Session, name: str) -> dict[str, str | list[str]] | None:
    """Search for a planet by name and return their details."""

    if (response := get_handles_exception(session, f"{BASE_URL}planets/?search={name}")) is not None:
        planet: dict[str, str | list[str]] = dict(Planet(**response.json()["results"][0]))
        planet["residents"] = [str(search_character_name_by_url(session, resident)) for resident in planet["residents"]]
        planet["films"] = [str(search_film_name_by_url(session, film)) for film in planet["films"]]
        return planet
    return None
