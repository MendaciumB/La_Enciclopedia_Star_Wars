from  httpx import Client as Session
from .species_functions.species_func import search_species_by_name, species_page_list, species_total_pages

def species_search(swapi_service: Session):
    total_pages: int = species_total_pages(swapi_service)
    current_page: int = 1

    while True:
        if (page := species_page_list(swapi_service, current_page)) is not None:
            print("\n", page)
        print(f"Page {current_page}/{total_pages}")

        action = input("\nEnter 'n' for next page, 'p' for previous page, 'd' for details, or 'exit' to quit: ")

        if action.lower() == 'n' and current_page < total_pages:
            current_page += 1
        elif action.lower() == 'p' and current_page > 1:
            current_page -= 1
        elif action.lower() == 'd':
            search_query = input("Enter species name to search (or 'exit' to quit): ")
            if search_query.lower() == 'exit':
                pass
            else:
                try:
                    species = search_species_by_name(swapi_service, search_query.replace(" ", "%20"))
                    print(f"\n{species}")
                except:
                    print("Species not found.")
        elif action.lower() == 'exit':
            break
        else:
            print("Invalid action.")
