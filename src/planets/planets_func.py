from httpx import Client as Session
from typing import Any
from src.models.planet import Planet
from src.models.data_interface import fields_update, load_data
from src.utils.search_name import search_info_by_name
from src.constants.constants import BASE_URL, PLANETS


url = f"{BASE_URL}{PLANETS}"

def search_planet_by_name(session: Session, name: str) -> dict[str, Any]:
    """Search for a character by name and return their details."""

    info = search_info_by_name(session, url, name)
    character = load_data(info, Planet)
    return fields_update(session, character).model_dump(exclude_defaults=True)