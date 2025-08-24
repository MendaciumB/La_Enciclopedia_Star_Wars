from .data_interface import Fields

class Character(Fields):
    """Model for Star Wars characters."""
    name: str
    height: str | None = None
    mass: str | None = None
    hair_color: str | None = None
    skin_color: str | None = None
    eye_color: str | None = None
    birth_year: str | None = None
    gender: str | None = None
