import httpx
from idk.characters.characters_search import character_search
from idk.films.film_search import film_search
from idk.starships.starship_search import starship_search
from idk.vehicles.vehicle_search import vehicle_search
from idk.species.species_search import species_search
from idk.planets.planets_search import planets_search

def main():
    swapi_service: httpx.Client = httpx.Client()
    print("\nStar Wars Character Search")
    
    while True:
        selection = input("\nWhat want to search? " \
                        "\n1. Characters " \
                        "\n2. Films " \
                        "\n3. Starships " \
                        "\n4. Vehicles " \
                        "\n5. Species " \
                        "\n6. Planets " \
                        "\nSelect a option or \"exit\" to quit: ")
        
        if selection == '1':
            print("\nLoading characters...")
            character_search(swapi_service)
            print("\nThank you for using the Star Wars Character Search!")
        elif selection == '2':
            print("\nLoading films...")
            film_search(swapi_service)
            print("\nThank you for using the Star Wars Film Search!")
        elif selection == '3':
            print("\nLoading starships...")
            starship_search(swapi_service)
            print("\nThank you for using the Star Wars Starship Search!")
        elif selection == '4':
            print("\nLoading vehicles...")
            vehicle_search(swapi_service)
            print("\nThank you for using the Star Wars Vehicle Search!")
        elif selection == '5':
            print("\nLoading species...")
            species_search(swapi_service)
            print("\nThank you for using the Star Wars Species Search!")
        elif selection == '6':
            print("\nLoading planets...")
            planets_search(swapi_service)
            print("\nThank you for using the Star Wars Planet Search!")
        elif selection.lower() == 'exit':
            break
    
    swapi_service.close()
    print("Goodbye!")




if __name__ == "__main__":
    main()