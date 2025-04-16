from httpx import Client as Session
from ...schemas.handles_exception import get_handles_exception


def search_species_name_by_url(session: Session, url: str) ->  str | None:
    """Search for a specie by URL and return their name."""

    if (response := get_handles_exception(session, url)) is not None:
        return response.json()["name"]
    return None
