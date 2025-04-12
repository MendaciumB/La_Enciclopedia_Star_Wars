from httpx import Client as Session
from ...schemas.handles_exception import get_handles_exception
from ...characters.characters_functions.character_name_by_id import search_character_name_by_id
from ...films.films_functions.film_func import search_film_name_by_id
from ..models.species import Species
from ...constants.constants import BASE_URL

def species_list(session: Session) -> list[str]:
    """Get a list of species names from the Star Wars API."""

    page: int = 1
    names: list[str] = []
    while page < 5:
        if (response := get_handles_exception(session, f"{BASE_URL}species/?page={page}")) is not None:
            for species in response.json()["results"]:
                names.append(species["name"])
        page += 1
    return names

def species_pages_list(session: Session) -> list[list[str]]:
    """This function divides the list of species names into pages of 10 names each."""

    names: list[str] = species_list(session)
    pages: list[list[str]] = []
    for i in range(0, len(names), 10):
        pages.append(names[i:i + 10])
    return pages

def search_species_by_name(session: Session, name: str) -> dict[str, str | list[str]] | None:
    """Search for a species by name and return their details."""

    if (response := get_handles_exception(session, f"{BASE_URL}species/?search={name}")) is not None:
        species: dict[str, str | list[str]] = dict(Species(**response.json()["results"][0]))
        species["people"] = [str(search_character_name_by_id(session, int(person.split("/")[-2]))) for person in species["people"]]
        species["films"] = [str(search_film_name_by_id(session, int(film.split("/")[-2]))) for film in species["films"]]
        return species
    return None

def search_species_name_by_id(session: Session, id: int) -> str | None:
    """Search for a species by ID and return their name."""

    if (response := get_handles_exception(session, f"{BASE_URL}species/{id}/")) is not None:
        return response.json()["name"]
    return None