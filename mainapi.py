import json
import requests

#Define the base URL endpoint for the API

base_url = "https://api.potterdb.com/v1"

#All the endpoints available in the API

endpoints = ["books","chapters", "characters", "movies", "spells", "potions"]

for endpoint in endpoints:
    #Constructing the full URL for the endpoint
    url = f"{base_url}/{endpoint}"
    
    #Making a GET request to the API endpoint
    response = requests.get(url,timeout=10) 
     # Added a timeout of 10 seconds to avoid hanging requests
    
    #Checking if the request was successful
    if response.status_code == 200:
        data = response.json()
        print(f"Data from {endpoint}:")
        print(json.dumps(data, indent=2))
    else:
        print(f"Failed to retrieve data from {endpoint}. Status code: {response.status_code}")






