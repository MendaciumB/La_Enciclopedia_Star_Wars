from httpx import Client as Session
from ...schemas.handles_exception import get_handles_exception
from ...films.films_functions.film_func import search_film_name_by_id
from ...starships.starships_functions.starships_func import search_starship_name_by_id
from ...vehicles.vehicles_functions.vehicles_func import search_vehicle_name_by_id
from ...species.species_functions.species_func import search_species_name_by_id
from ...planets.planets_functions.planets_func import search_planet_name_by_id
from ..models.character import Character
from ...constants.constants import BASE_URL


def characters_list(session: Session) -> list[str]:
    """Get a list of character names from the Star Wars API."""

    page: int = 1
    names: list[str] = []
    while page < 10:
        if (response := get_handles_exception(session, f"{BASE_URL}people/?page={page}")) is not None:
            for character in response.json()["results"]:
                names.append(character["name"])
        page += 1
    return names  


def character_pages_list(session: Session) -> list[list[str]]:
    """This function divides the list of character names into pages of 10 names each."""
    
    names: list[str] = characters_list(session)
    pages: list[list[str]] = []
    for i in range(0, len(names), 10):
        pages.append(names[i:i + 10])
    return pages


def search_character_by_name(session: Session, name: str) -> dict[str, str | list[str]] | None:
    """Search for a character by name and return their details."""

    if (response := get_handles_exception(session, f"{BASE_URL}people/?search={name}")) is not None:
        character: dict[str, str | list[str]] = dict(Character(**response.json()["results"][0]))
        character["films"] = [str(search_film_name_by_id(session, int(film.split("/")[-2]))) for film in character["films"]]
        character["species"] = [str(search_species_name_by_id(session, int(species.split("/")[-2]))) for species in character["species"]]
        character["vehicles"] = [str(search_vehicle_name_by_id(session, int(vehicle.split("/")[-2]))) for vehicle in character["vehicles"]]
        character["starships"] = [str(search_starship_name_by_id(session, int(starship.split("/")[-2]))) for starship in character["starships"]]
        character["homeworld"] = str(search_planet_name_by_id(session, int(str(character["homeworld"]).split("/")[-2])))
        return character
    return None
