from httpx import Client as Session
from typing import Any
from src.utils.search_name import search_info_by_name
from src.models.character import Character
from src.models.data_interface import fields_update
from src.constants.constants import BASE_URL, CHARACTERS


def load_character(payload: dict[str, Any]) -> Character:
    return Character(**payload)

url = f"{BASE_URL}{CHARACTERS}"

def search_character_by_name(session: Session, name: str) -> dict[str, Any] | None:
    """Search for a character by name and return their details."""

    info = search_info_by_name(session, url, name)
    character = load_character(info)
    return fields_update(session, character).model_dump(exclude_defaults=True)
