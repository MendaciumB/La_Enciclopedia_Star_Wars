from httpx import Client as Session
from src.films.films_func import search_film_by_title
from src.utils.total_values import url_values

def film_search(swapi_service: Session):
    while True:
        print("\n", films(swapi_service))
        action = input("\nEnter 'd' for details or 'exit' to quit: ")
        if action.lower() == 'd':
            search_query = input("\nEnter character name to search (or 'exit' to quit): ")
            if search_query.lower() == 'exit':
                pass
            else:
                try:
                    film = search_film_by_title(swapi_service, search_query)
                    print(f"\n{film}")
                except:
                    print("Film not found.")
        elif action.lower() == 'exit':
            break

def films(session: Session) -> list[str]:
    target = "films"
    films = []
    values = url_values(session, target)
    for i in values:
        films.append(i.get('title'))
    return films