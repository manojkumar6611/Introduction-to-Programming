import requests

def search_species(city):
    # Dummy data for demonstration purposes
    return [
        {"Species": {"AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
        {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}}
    ]

def filter_venomous(species_list):
    return [species for species in species_list if species["Species"]["PestStatus"] == "Venomous"]
