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
    
    filename = "harry_potter_books.json"
    with open(filename, "w", encoding="utf-8") as json_file:
      json.dump(books, json_file, indent=4)

    print(
        f"Successfully saved {len(books)} books to '{filename}'!"
    )

    
    print("\nPreview of the first book:")
    print(json.dumps(books[0], indent=4))
  else:
    print("No books were returned.")

except requests.exceptions.RequestException as error:
  print(f"Request failed: {error}")

except (ValueError, KeyError, IndexError, TypeError) as error:
  print(f"Could not process the returned data: {error}")