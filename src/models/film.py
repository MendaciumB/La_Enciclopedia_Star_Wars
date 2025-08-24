from .data_interface import Fields


class Film(Fields):
    title: str
    episode_id: int
    director: str
    producer: str
    release_date: str