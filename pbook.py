import json
import requests

api_url = "https://openlibrary.org/search.json?q=harry+potter"

try:
  
  response = requests.get(
      api_url,
      timeout=10,  
  )
  response.raise_for_status()
  search_data = response.json()
  books = search_data.get("docs", [])
  if books:
        
    print("\nPreview of the first book:")
    print(json.dumps(books[0], indent=4))
  else:
    print("No books were returned.")

except requests.exceptions.RequestException as error:
  print(f"Request failed: {error}")

except (ValueError, KeyError, IndexError, TypeError) as error:
  print(f"Could not process the returned data: {error}")

  '''
• ValueError: Triggers if response.json() tries to parse the text, but the server sent back broken, invalid JSON text 
• KeyError: Triggers if you try to look up a specific field that doesn't exist 
• IndexError: Triggers if you try to access a specific item in a list that isn't there 
• TypeError: Triggers if you try to treat the data incorrectly 
  '''