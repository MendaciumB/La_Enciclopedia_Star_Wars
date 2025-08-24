from typing_extensions import deprecated
from typing import Union
from httpx import Client as Session
from src.schemas.handles_exception import get_handles_exception
from src.constants.constants import BASE_URL, PAGINATION


def url_values(session: Session, target: str) -> list[dict[str, Union[str, list[str]]]]:
    """Get the url values from the Star Wars API."""
    if (response := get_handles_exception(session, f"{BASE_URL}{target}")):
        values: list[dict[str, Union[str, list[str]]]] = response.json()
    return values

@deprecated("use len(url_values()) instead")
def total_values(session: Session, target: str) -> int:
    values = url_values(session, target)
    return len(values)

def total_pages(session: Session, target: str) -> tuple[int, list[dict[str, Union[str, list[str]]]]]:
    values = url_values(session, target)
    l_values = len(values)
    if l_values % 10 != 0:
        t_pages = l_values//PAGINATION + 1
    else:
        t_pages = l_values//PAGINATION
    return (t_pages, values)

def pages_values(session: Session, target: str) -> tuple[list[list[str]], int]:
    """The func to use in logic"""
    t_pages, values = total_pages(session, target)
    pages: list[list[str]] = []
    index = 0
    for _ in range(t_pages):
        arr = []
        for _ in range(10):
            try: 
                name = values[index].get('name')
            except:
                break
            arr.append(name)
            index += 1
        pages.append(arr)
    return (pages, t_pages)
