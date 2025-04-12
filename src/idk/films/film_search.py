from httpx import Client as Session
from ..films.films_functions.film_func import films_pages_list, search_film_by_title

def film_search(swapi_service: Session):
    while True:
        print("\n", films_pages_list(swapi_service))
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




    # pages: list[list[str]] = pages_list(swapi_service)
    # total_pages: int = len(pages)
    # current_page: int = 1
    
    # while True:
    #     print("\n", pages[current_page - 1])
    #     print(f"Page {current_page}/{total_pages}")

    #     action = input("\nEnter 'n' for next page, 'p' for previous page, 'd' for details, or 'exit' to quit: ")

    #     if action.lower() == 'n' and current_page < total_pages:
    #         current_page += 1
    #     elif action.lower() == 'p' and current_page > 1:
    #         current_page -= 1
    #     elif action.lower() == 'd':
    #         search_query = input("Enter character name to search (or 'exit' to quit): ")
    #         if search_query.lower() == 'exit':
    #             pass
    #         else:
    #             try:
    #                 character = search_character_by_name(swapi_service, search_query.replace(" ", "%20"))
    #                 print(f"\n{character}")
    #             except:
    #                 print("Character not found.")
    #     elif action.lower() == 'exit':
    #         break
    #     else:
    #         print("Invalid action.")