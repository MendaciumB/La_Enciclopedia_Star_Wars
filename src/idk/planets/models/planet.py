from pydantic import BaseModel

class Planet(BaseModel):
    """Model representing a planet in the Star Wars universe."""

    name: str
    rotation_period: str
    orbital_period: str
    diameter: int
    climate: str
    gravity: str
    terrain: str
    surface_water: str
    population: str
    residents: list[str]
    films: list[str]