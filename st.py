
import requests
import json

# 1. URL of the external country API. This simply defines the endpoint for retrieving information about Nigeria. An endpoint is a URL that identifies a particular API resource or operation.
api_url = (
    "https://api.restcountries.com/countries/v5/names.common/Nigeria"
)

# 2. Authentication header. Headers carry additional information about the request. An authorization header supplies credentials when the API requires them.
headers = {
    "Authorization": "Bearer rc_live_demo"
}

try:
    # 3. Send the HTTPS GET request.
    response = requests.get(   #sends an HTTP GET request.
        api_url,   #specifies where to send it.
        headers=headers, #provides request metadata and authentication.
        timeout=10   #limits how long the program waits for the request.
    )

    # 4. Check for HTTP errors, such as 401.
    response.raise_for_status()

    # 5. Convert the JSON response into Python data.
    country_data = response.json()

    # 6. Check for API-level errors.
    if country_data.get("errors"):
        for error in country_data["errors"]:
            print("API error:", error.get("message", "Unknown error"))

    else:
        # 7. Extract the list of country records.
        countries = country_data["data"]["objects"]

        if countries:
            nigeria = countries[0]

            print("Selected country:")
            print(json.dumps(nigeria, indent=4))
        else:
            print("No country was returned.")

except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")

except (ValueError, KeyError, IndexError, TypeError) as error:
    print(f"Could not process the returned data: {error}")
