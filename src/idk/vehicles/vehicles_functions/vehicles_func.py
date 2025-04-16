import math
from httpx import Client as Session
from ...schemas.handles_exception import get_handles_exception
from ...characters.characters_functions.character_name import search_character_name_by_url
from ...films.films_functions.film_name import search_film_name_by_url
from ..models.vehicle import Vehicle
from ...constants.constants import BASE_URL, PAGINATION


def vehicles_total_pages(session: Session) -> int:
    """Get the total number of pages of vehicles from the Star Wars API."""
    total_pages: int = 1
    if (response := get_handles_exception(session, f"{BASE_URL}people/?page={total_pages}")) is not None:
        result = response.json()
        total_pages = math.ceil(result["count"]/PAGINATION)
    return total_pages


def vehicles_page_list(session: Session, page: int) -> list[str] | None:
    """Get a list of vehicle names of a page from the Star Wars API."""

    if (response := get_handles_exception(session, f"{BASE_URL}vehicles/?page={page}")) is not None:
        return [vehicle["name"] for vehicle in response.json()["results"]]
    return None


def search_vehicle_by_name(session: Session, name: str) -> dict[str, str | list[str]] | None:
    """Search for a vehicle by name and return their details."""

    if (response := get_handles_exception(session, f"{BASE_URL}vehicles/?search={name}")) is not None:
        vehicle: dict[str, str | list[str]] = dict(Vehicle(**response.json()["results"][0]))
        vehicle["pilots"] = [str(search_character_name_by_url(session, pilot)) for pilot in vehicle["pilots"]]
        vehicle["films"] = [str(search_film_name_by_url(session, film)) for film in vehicle["films"]]
        return vehicle
    return None
