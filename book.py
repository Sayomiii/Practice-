import requests  #Imports the requests library, which allows your Python program to send HTTP/HTTPS requests to websites and APIs.
import json    #mports Python's built-in json module, used for handling JSON data (parsing it or converting dictionaries into nicely formatted text).


#URL of the external country API. This simply defines the endpoint for retrieving information about Nigeria. An endpoint is a URL that identifies a particular API resource or operation.
api_url = (
    "https://openlibrary.org/search.json?q=harry+potter"
)


try: #This starts a block of code where errors might happen. If anything goes wrong inside this block, Python jumps straight to the except blocks instead of crashing.


    # Send the HTTPS GET request.
    response = requests.get(   #sends an HTTP GET request.
        api_url,   #specifies where to send it.
        timeout=10   #limits how long the program waits for the request.
    )

    # 4. Check for HTTP errors, such as 401.
    response.raise_for_status()

    # 5. Convert the JSON response into Python data.
    search_data = response.json()
    books = search_data.get("docs", [])

    if books:
        first_book = books[0]
        print("Selected book:")
        print(json.dumps(first_book, indent=4))
    else:
        print("No books were returned.")
except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")

except (ValueError, KeyError, IndexError, TypeError) as error:
    print(f"Could not process the returned data: {error}")