from httpx import Client as Session
from .films_functions.films_func import films_list, search_film_by_title

def film_search(swapi_service: Session):
    while True:
        print("\n", films_list(swapi_service))
        action = input("\nEnter 'd' for details or 'exit' to quit: ")
        if action.lower() == 'd':
            search_query = input("\nEnter character name to search (or 'exit' to quit): ")
            if search_query.lower() == 'exit':
                pass
            else:
                try:
                    film = search_film_by_title(swapi_service, search_query.replace(" ", "%20"))
                    print(f"\n{film}")
                except:
                    print("Film not found.")
        elif action.lower() == 'exit':
            break
