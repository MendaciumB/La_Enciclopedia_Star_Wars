import math
from httpx import Client as Session
from ...schemas.handles_exception import get_handles_exception
from ...films.films_functions.film_name import search_film_name_by_url
from ...starships.starships_functions.starship_name import search_starship_name_by_url
from ...vehicles.vehicles_functions.vehicle_name import search_vehicle_name_by_url
from ...species.species_functions.specie_name import search_species_name_by_url
from ...planets.planets_functions.planet_name import search_planet_name_by_url
from ..models.character import Character
from ...constants.constants import BASE_URL, PAGINATION


def character_total_pages(session: Session) -> int:
    """Get the total number of pages of characters from the Star Wars API."""
    total_pages: int = 1
    if (response := get_handles_exception(session, f"{BASE_URL}people/?page={total_pages}")) is not None:
        result = response.json()
        total_pages = math.ceil(result["count"]/PAGINATION)
    return total_pages


def character_page_list(session: Session, page: int) -> list[str] | None:
    """Get a list of character names of a page from the Star Wars API."""

    if (response := get_handles_exception(session, f"{BASE_URL}people/?page={page}")) is not None:
        return [character["name"] for character in response.json()["results"]]
    return None


def search_character_by_name(session: Session, name: str) -> dict[str, str | list[str]] | None:
    """Search for a character by name and return their details."""

    if (response := get_handles_exception(session, f"{BASE_URL}people/?search={name}")) is not None:
        character: dict[str, str | list[str]] = dict(Character(**response.json()["results"][0]))
        if "films" in character:
            character["films"] = [str(search_film_name_by_url(session, film)) for film in character["films"]]
        if "species" in character:
            character["species"] = [str(search_species_name_by_url(session, species)) for species in character["species"]]
        if "vehicles" in character:
            character["vehicles"] = [str(search_vehicle_name_by_url(session, vehicle)) for vehicle in character["vehicles"]]
        if "starships" in character:
            character["starships"] = [str(search_starship_name_by_url(session, starship)) for starship in character["starships"]]
        if "homeworld" in character:
            character["homeworld"] = str(search_planet_name_by_url(session, str(character["homeworld"])))
        return character
    return None



# implementar dic especificando los valores
# generar una clase que se llame película
# pensar descripciones
# url en vez de split
# hacer dinámico la pages
# subir a git v2