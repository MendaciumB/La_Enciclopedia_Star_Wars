import math
from httpx import Client as Session
from ...schemas.handles_exception import get_handles_exception
from ...characters.characters_functions.character_name import search_character_name_by_url
from ...films.films_functions.film_name import search_film_name_by_url
from ..models.species import Species
from ...constants.constants import BASE_URL, PAGINATION


def species_total_pages(session: Session) -> int:
    """Get the total number of pages of species from the Star Wars API."""
    total_pages: int = 1
    if (response := get_handles_exception(session, f"{BASE_URL}people/?page={total_pages}")) is not None:
        result = response.json()
        total_pages = math.ceil(result["count"]/PAGINATION)
    return total_pages


def species_page_list(session: Session, page: int) -> list[str] | None:
    """Get a list of species names of a page from the Star Wars API."""

    if (response := get_handles_exception(session, f"{BASE_URL}species/?page={page}")) is not None:
        return [species["name"] for species in response.json()["results"]]
    return None


def search_species_by_name(session: Session, name: str) -> dict[str, str | list[str]] | None:
    """Search for a species by name and return their details."""

    if (response := get_handles_exception(session, f"{BASE_URL}species/?search={name}")) is not None:
        species: dict[str, str | list[str]] = dict(Species(**response.json()["results"][0]))
        species["people"] = [str(search_character_name_by_url(session, person)) for person in species["people"]]
        species["films"] = [str(search_film_name_by_url(session, film)) for film in species["films"]]
        return species
    return None
