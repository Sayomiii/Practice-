import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key= os.getenv("WEATHER_API_KEY")
api_url="https://api.weatherapi.com/v1/current.json"

if not api_key:
    print("API key is not available, Check .env file.")
else:
    api_url=f"{api_url}?key={api_key}&q=London&aqi=no"
    print("API URL successful")

#TO MAKE REQUEST AND TRY ERROR HANDLING
try:
    response=requests.get(api_url, timeout=15)
    response.raise_for_status()
    feed=response.json()
    """
To open a file called london_weather.json and write the feed to it in json format with indentation of 4 spaces and ensure_ascii set to False
    """
    with open("london_weather.json", "w", encoding="utf-8") as file:
        json.dump(feed, file, indent=4, ensure_ascii=False)
    print("Weather feed saved to weather.json")
    print("Location:", feed["location"]["name"])
    print("Temperature:", feed["current"]["temp_c"], "C")
    print("Condition:", feed["current"]["condition"]["text"])
    print("London Weather feed extracted successfully")

except requests.exceptions.Timeout:
    print("The request is timed out. Try again.")
except requests.exceptions.HTTPError as error:
    print("An HTTP error occured: {error}")
except requests.exceptions.RequestException as error:
    print("An API request error occured: {error}")
except ValueError:
    print("The API response cannot be decoded to json")
except (KeyError, TypeError):
    print("The API response is missing expected data")


