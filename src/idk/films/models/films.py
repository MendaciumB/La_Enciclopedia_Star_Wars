from pydantic import BaseModel

class Films(BaseModel):
    title: str
    episode_id: int
    director: str
    producer: str
    release_date: str