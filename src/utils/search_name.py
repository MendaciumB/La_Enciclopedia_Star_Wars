from httpx import Client as Session
from typing import Any
from src.schemas.handles_exception import get_handles_exception

def search_field_by_url(session: Session, url: str, name: str = "name") -> str:
    """Search for a json by URL and return their name."""

    response = get_handles_exception(session, url)
    return response.json().get(name)

def search_info_by_name(session: Session, url: str, name: str, is_film: bool = False) -> dict[str, Any]:
    response = get_handles_exception(session, url)
    data: dict[str, str]
    if is_film:
        for i in response.json():
            if i["title"] == name:
                data = i
                break
    elif not is_film:
        for i in response.json():
            if i["name"] == name:
                data = i
                break
    else:
        raise Exception("Name not found")
    return data
