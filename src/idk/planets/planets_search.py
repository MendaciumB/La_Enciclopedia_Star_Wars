from  httpx import Client as Session
from .planets_functions.planets_func import search_planet_by_name, planets_pages_list


def planets_search(swapi_service: Session):
    """Search for planets in the Star Wars API."""

    pages: list[list[str]] = planets_pages_list(swapi_service)
    total_pages: int = len(pages)
    current_page: int = 1

    while True:
        print("\n", pages[current_page - 1])
        print(f"Page {current_page}/{total_pages}")

        action = input("\nEnter 'n' for next page, 'p' for previous page, 'd' for details, or 'exit' to quit: ")

        if action.lower() == 'n' and current_page < total_pages:
            current_page += 1
        elif action.lower() == 'p' and current_page > 1:
            current_page -= 1
        elif action.lower() == 'd':
            search_query = input("Enter planet name to search (or 'exit' to quit): ")
            if search_query.lower() == 'exit':
                pass
            else:
                try:
                    planet = search_planet_by_name(swapi_service, search_query.replace(" ", "%20"))
                    print(f"\n{planet}")
                except:
                    print("Planet not found.")
        elif action.lower() == 'exit':
            break
        else:
            print("Invalid action.")