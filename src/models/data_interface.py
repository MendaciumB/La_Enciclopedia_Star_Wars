from pydantic import BaseModel, HttpUrl
from httpx import Client as Session
from src.utils.search_name import search_field_by_url

class Fields(BaseModel):
    homeworld: str | None = None
    characters: list[HttpUrl] | list[str] | list[None] | None = None
    films: list[HttpUrl] | list[str] | list[None] | None = None
    planets: list[HttpUrl] | list[str] | list[None] | None = None
    species: list[HttpUrl] | list[str] | list[None] | None = None
    vehicles: list[HttpUrl] | list[str] | list[None] | None = None
    starships: list[HttpUrl] | list[str] | list[None] | None = None
    pilots: list[HttpUrl] | list[str] | list[None] | None = None
    people: list[HttpUrl] | list[str] | list[None] | None = None
    residents: list[HttpUrl] | list[str] | list[None] | None = None



def search_for_each(session: Session, payload: list[HttpUrl] | list[str] | list[None], name: str = "name") -> list[str]:
    return [search_field_by_url(session, str(i), name) for i in payload]

def fields_update(session: Session, payload: Fields) -> Fields:
    if payload.homeworld:
        payload.homeworld = search_field_by_url(session, str(payload.homeworld))

    if payload.characters:
        payload.characters = search_for_each(session, payload.characters)

    if payload.films:
        payload.films = search_for_each(session, payload.films, "title")

    if payload.planets:
        payload.planets = search_for_each(session, payload.planets)

    if payload.species:
        payload.species = search_for_each(session, payload.species)

    if payload.vehicles:
        payload.vehicles = search_for_each(session, payload.vehicles)

    if payload.starships:
        payload.starships = search_for_each(session, payload.starships)

    if payload.pilots:
        payload.pilots = search_for_each(session, payload.pilots)

    if payload.people:
        payload.people = search_for_each(session, payload.people)

    if payload.residents:
        payload.residents = search_for_each(session, payload.residents)

    return payload
