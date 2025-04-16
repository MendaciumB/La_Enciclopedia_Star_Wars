from httpx import Client as Session
from .characters_functions.characters_func import search_character_by_name, character_page_list, character_total_pages

def character_search(swapi_service: Session):
    current_page: int = 1
    total_pages: int = character_total_pages(swapi_service)
    
    while True:
        if (page := character_page_list(swapi_service, current_page)) is not None:
            print("\n", page)
        print(f"Page {current_page}/{total_pages}")

        action = input("\nEnter 'n' for next page, 'p' for previous page, 'd' for details, or 'exit' to quit: ")

        if action.lower() == 'n' and current_page < total_pages:
            current_page += 1
        elif action.lower() == 'p' and current_page > 1:
            current_page -= 1
        elif action.lower() == 'd':
            search_query = input("Enter character name to search (or 'exit' to quit): ")
            if search_query.lower() == 'exit':
                pass
            else:
                try:
                    character = search_character_by_name(swapi_service, search_query.replace(" ", "%20"))
                    print(f"\n{character}")
                except:
                    print("Character not found.")
        elif action.lower() == 'exit':
            break
        else:
            print("Invalid action.")