##def display_menu():
    
    ##print("Help")
    ##print("====")
    ##print("The following commands are recognized:")
    ##print("a. Display help")
    ##print("b. Exit the program")
##display_menu()
def display_menu():
    """Display the help menu."""
    print("Welcome to the Wildlife Tracker!")
    print("Available commands:")
    print("  help - Display this help menu")
    print("  exit - Exit the program")
    print("  list - List all available species")
    print("  search <species_name> - Search for a specific species")
    print("  locate <city> - Get GPS coordinates for a city")
    print("  sightings <species_name> - List sightings of a specific species")
    print("  nearest <city> - Find the nearest wildlife sighting to a city")
    print("  report - Report a new wildlife sighting")
display_menu()

def main():
    while True:
        user_input = input("wildlife> ")
    
        if user_input == "help":
            display_menu()
        elif user_input == "exit":
            print("Exiting the program...")
            break
        else:
            print("Invalid command. Type 'help' for assistance.")

main()
def search_species(city):
 # Stub function: return a list of species
 return [
 {"Species": {"AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
 {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}}
 ]
def display_species(species_list):
 # Print the list of species
 for species in species_list:
    print(species["Species"]["AcceptedCommonName"])
# Test the functions
city = "Cairns"
species_list = search_species(city)
display_species(species_list)
def search_sightings(taxonid, city):
 # Stub function: return a list of animal sightings
 return [{"properties": {"StartDate": "1999-11-15", "LocalityDetails": "Tinaroo"}}]
def display_sightings(sightings):
 # Print the list of sightings
 for sighting in sightings:
    print("Date:", sighting["properties"]["StartDate"])
    print("Location:", sighting["properties"]["LocalityDetails"])
# Test the functions
taxonid = 1039
city = "Cairns"
sightings = search_sightings(taxonid, city)
display_sightings(sightings)
def filter_venomous(species_list):
    # Filter and return only venomous species
    venomous_species = []
    for species in species_list:
        if species["Species"]["PestStatus"] == "Venomous":
            venomous_species.append(species)
    return venomous_species

# Test the function
species_list = [
    {"Species": {"AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
    {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}}
]
venomous_species = filter_venomous(species_list)
print(venomous_species)
def gps(city):
 # Stub function: return Brisbane's GPS coordinates
 return {"latitude": -27.4689682, "longitude": 153.0234991}
# Test the function
city = "Cairns"
coordinates = gps(city)
print("GPS coordinates for", city + ":", coordinates)
import requests

def gps_coordinate(city):
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    response = requests.get(url)
    data = response.json()
    if data:
        return {"latitude": float(data[0]["lat"]), "longitude": float(data[0]["lon"])}

# Test the function
city = "Cairns"
coordinates = gps_coordinate(city)
print("GPS coordinates for", city + ":", coordinates)
import requests

def get_species_list(coordinate, radius):
    url = f"https://apps.des.qld.gov.au/species/?op=getspecieslist&kingdom=animals&circle={coordinate['latitude']},{coordinate['longitude']},{radius}"
    response = requests.get(url)
    data = response.json()
    if "SpeciesSightingSummariesContainer" in data:
        return data["SpeciesSightingSummariesContainer"]["SpeciesSightingSummary"]

# Test the function
coordinate = {"latitude": -27.4689682, "longitude": 153.0234991}
radius = 100000
species_list = get_species_list(coordinate, radius)
print("Species List:", species_list)
import requests
import time

def gps_coordinate(city):
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    
    for _ in range(3):  # Retry up to 3 times
        response = requests.get(url)
        if response.status_code == 200:
            try:
                data = response.json()
                if data:
                    return {"latitude": float(data[0]["lat"]), "longitude": float(data[0]["lon"])}
                else:
                    print("Error: Empty response from API")
            except json.decoder.JSONDecodeError:
                print("Error: Unable to decode JSON response")
        else:
            print("Error: API request failed with status code", response.status_code)
        
        # Wait before retrying
        time.sleep(2)
    
    print("Error: Maximum retries exceeded")
    return None

# Test the function
city = "Cairns"
coordinates = gps_coordinate(city)
print("GPS coordinates for", city + ":", coordinates)

import requests

def get_surveys_by_species(coordinate, radius, taxonid):
    url = f"https://apps.des.qld.gov.au/species/?op=getsurveysbyspecies&taxonid={taxonid}&circle={coordinate['latitude']},{coordinate['longitude']},{radius}"
    response = requests.get(url)
    data = response.json()
    if "features" in data:
        return data["features"]

# Test the function
coordinate = {"latitude": -27.4689682, "longitude": 153.0234991}
radius = 100000
taxonid = 1039
surveys = get_surveys_by_species(coordinate, radius, taxonid)
print("Surveys:", surveys)
# Define sightings data
sightings = [
    {"properties": {"StartDate": "2022-05-10", "LocalityDetails": "Location A"}},
    {"properties": {"StartDate": "2022-04-15", "LocalityDetails": "Location B"}},
    {"properties": {"StartDate": "2022-06-20", "LocalityDetails": "Location C"}}
]
def earliest(sightings):
    # Initialize earliest sighting with a placeholder value
    earliest_sighting = None
    
    # Iterate through the sightings to find the earliest sighting
    for sighting in sightings:
        start_date = sighting["properties"]["StartDate"]
        if earliest_sighting is None or start_date < earliest_sighting:
            earliest_sighting = start_date
    
    return earliest_sighting


# Call earliest function
earliest_sighting = earliest(sightings)
print("Earliest Sighting:", earliest_sighting)

# Call display_sightings function
display_sightings(sightings)

