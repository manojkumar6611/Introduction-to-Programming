import requests

def gps_coordinate(city): 
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        
        data = response.json()
        
        if data:
            return {"latitude": float(data[0]["lat"]), "longitude": float(data[0]["lon"])}
        else:
            print("No data found for the city:", city)
            return None
    except requests.exceptions.RequestException as err:
        print("Error fetching data:", err)
        return None
    except (IndexError, KeyError) as err:
        print("Error parsing data:", err)
        return None

