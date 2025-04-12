from httpx import Client as Session
from ...schemas.handles_exception import get_handles_exception
from ...characters.characters_functions.character_name_by_id import search_character_name_by_id
from ...films.films_functions.film_func import search_film_name_by_id
from ..models.vehicle import Vehicle
from ...constants.constants import BASE_URL

def vehicles_list(session: Session) -> list[str]:
    """Get a list of vehicle names from the Star Wars API."""

    page: int = 1
    names: list[str] = []
    while page < 5:
        if (response := get_handles_exception(session, f"{BASE_URL}vehicles/?page={page}")) is not None:
            for vehicle in response.json()["results"]:
                names.append(vehicle["name"])
        page += 1
    return names

def vehicles_pages_list(session: Session) -> list[list[str]]:
    """This function divides the list of vehicle names into pages of 10 names each."""

    names: list[str] = vehicles_list(session)
    pages: list[list[str]] = []
    for i in range(0, len(names), 10):
        pages.append(names[i:i + 10])
    return pages

def search_vehicle_by_name(session: Session, name: str) -> dict[str, str | list[str]] | None:
    """Search for a vehicle by name and return their details."""

    if (response := get_handles_exception(session, f"{BASE_URL}vehicles/?search={name}")) is not None:
        vehicle: dict[str, str | list[str]] = dict(Vehicle(**response.json()["results"][0]))
        vehicle["pilots"] = [str(search_character_name_by_id(session, int(pilot.split("/")[-2]))) for pilot in vehicle["pilots"]]
        vehicle["films"] = [str(search_film_name_by_id(session, int(film.split("/")[-2]))) for film in vehicle["films"]]
        return vehicle
    return None

def search_vehicle_name_by_id(session: Session, id: int) -> str | None:
    """Search for a vehicle by ID and return their name."""

    if (response := get_handles_exception(session, f"{BASE_URL}vehicles/{id}/")) is not None:
        return response.json()["name"]
    return None