import requests

def display_menu():
    """Display the help menu."""
    print("Welcome to the Wildlife Tracker!")
    print("Available commands:")
    print("  help - Display this help menu")
    print("  exit - Exit the program")
    print("  list - List all available species")
    print("  sightings - display animal sightings in a city")
    print("  venomous - display venomous species")
    

def search_species(city):
    # Dummy data for demonstration purposes
    return [
        {"Species": {"AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
        {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}}
    ]

def display_species(species_list):
    # Print the list of species
    for species in species_list:
        print(species["Species"]["AcceptedCommonName"])
        # sightings=search_sightings(taxonid,city)
        # display_sightigs(sightings)

def get_surveys_by_species(coordinate, radius, taxonid):
    url = f"https://apps.des.qld.gov.au/species/?op=getsurveysbyspecies&taxonid={taxonid}&circle={coordinate['latitude']},{coordinate['longitude']},{radius}"
    response = requests.get(url)
    data = response.json()
    if "features" in data:
        return data["features"]

def gps_coordinate(city):
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    response = requests.get(url)
    data = response.json()
    if data:
        return {"latitude": float(data[0]["lat"]), "longitude": float(data[0]["lon"])}
    return None

def search_sightings(taxonid, city):
    # Stub function: return a list of animal sightings
    return [{"properties": {"StartDate": "1999-11-15", "LocalityDetails": "Tinaroo"}}]

def filter_venomous(species_list):
    return [{"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}}]

def display_venomous(species_list):
    for species in species_list:
        print(species["Species"]["AcceptedCommonName"], species["Species"]["PestStatus"])

def sort_by_date(sightings):
    """Returns sightings sorted by date."""
    return sorted(sightings, key=lambda x: x["properties"]["StartDate"])

def display_sightings(sightings):
    """Prints a list of animal sightings to the screen."""
    sorted_sightings = sort_by_date(sightings)
    for sighting in sorted_sightings:
        print(f"Start Date: {sighting['properties']['StartDate']}, Locality Details: {sighting['properties']['LocalityDetails']}")

def earliest(sightings):
    """Returns the sighting with the minimum start date."""
    earliest_sighting = None
    for sighting in sightings:
        if earliest_sighting is None or sighting["properties"]["StartDate"] < earliest_sighting["properties"]["StartDate"]:
            earliest_sighting = sighting
    return earliest_sighting

def main():
    display_menu()  # Show the menu at the start
    while True:
        user_input = input("wildlife> ").split()

        if len(user_input) == 0:
            continue

        command = user_input[0]

        if command == "help":
            display_menu()
        elif command == "exit":
            print("Exiting the program...")
            break
        elif command == "list":
            city = "Cairns"  # Example city for demonstration
            species_list = search_species(city)
            display_species(species_list)
        elif command == "sightings":
            taxonid = 1039  # Example taxon ID for demonstration
            city = "Cairns" #Example species name for demonstration
            sightings = search_sightings(taxonid,city)
            display_sightings(sightings)
        elif command == "venomous":
            city = "Cairns"
            species_list = search_species(city)
            filter_venomous(species_list)
            display_venomous(species_list)
        elif command == "search":
            if len(user_input) == 2:
                species_name = user_input[1]
                # Call function to search for a specific species
                # For now, we'll just print the species name for demonstration
                print(f"Searching for species: {species_name}")
            else:
                print("Usage: search <species_name>")
        elif command == "locate":
            if len(user_input) == 2:
                city = user_input[1]
                coordinates = gps_coordinate(city)
                if coordinates:
                    print(f"GPS coordinates for {city}: {coordinates}")
                else:
                    print(f"Could not find GPS coordinates for city: {city}")
            else:
                print("Usage: locate <city>")
        elif command == "sightings":
            if len(user_input) == 2:
                species_name = user_input[1]
                # Call function to list sightings of a specific species
                # For now, we'll just print the species name for demonstration
                print(f"Listing sightings for species: {species_name}")
                taxonid = 1039  # Example taxon ID for demonstrationhelp
                sightings = search_sightings(taxonid, species_name)
                display_sightings(sightings)
            else:
                print("Usage: sightings <species_name>")
        elif command == "nearest":
            if len(user_input) == 2:
                city = user_input[1]
                # Call function to find the nearest wildlife sighting to a city
                # For now, we'll just print the city name for demonstration
                print(f"Finding nearest wildlife sighting to city: {city}")
            else:
                print("Usage: nearest <city>")
        elif command == "report":
            # Call function to report a new wildlife sighting
            # For now, we'll just print a message for demonstration
            print("Reporting a new wildlife sighting")
        else:
            print("Invalid command. Type 'help' for assistance.")

main()

