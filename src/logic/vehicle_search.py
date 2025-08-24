from httpx import Client as Session
from src.vehicles.vehicles_func import search_vehicle_by_name
from src.utils.total_values import pages_values

def vehicle_search(swapi_service: Session):
    target = "vehicles"
    pages, t_pages = pages_values(swapi_service, target)
    current_page: int = 1
    
    while True:
        print("\n", pages[current_page - 1])
        print(f"Page {current_page}/{t_pages}")

        action = input("\nEnter 'n' for next page, 'p' for previous page, 'd' for details, or 'exit' to quit: ")

        if action.lower() == 'n' and current_page < t_pages:
            current_page += 1
        elif action.lower() == 'p' and current_page > 1:
            current_page -= 1
        elif action.lower() == 'd':
            search_query = input("Enter vehicle name to search (or 'exit' to quit): ")
            if search_query.lower() == 'exit':
                pass
            else:
                try:
                    vehicle = search_vehicle_by_name(swapi_service, search_query)
                    print(f"\n{vehicle}")
                except:
                    print("Vehicle not found.")
        elif action.lower() == 'exit':
            break
        else:
            print("Invalid action.")