from httpx import Client as Session
from ...schemas.handles_exception import get_handles_exception
from ...constants.constants import BASE_URL

def search_character_name_by_id(session: Session, id: int) -> str | None:
    """Search for a character by ID and return their name."""

    if (response := get_handles_exception(session, f"{BASE_URL}people/{id}/")) is not None:
        return response.json()["name"]
    return None