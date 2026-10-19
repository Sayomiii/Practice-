import json
from bs4 import BeautifulSoup
import requests

# Step 1: Request the Mattel Barbie page
# Using a User-Agent header helps mimic a real web browser to avoid immediate blocking.
url = "https://shop.mattel.com/collections/barbie"
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
        " like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}

print("Fetching the Barbie collection page...")
try:
  response = requests.get(url, headers=headers, timeout=15)
  response.raise_for_status()
except requests.exceptions.RequestException as e:
  print(f"Error fetching the page: {e}")
  exit()

# Step 2 & 3: Inspect HTML and Use Beautiful Soup to extract information
soup = BeautifulSoup(response.text, "html.parser")
products = []

# Note: E-commerce class names change frequently. 
# You should inspect the specific HTML tags on the live site to adjust these CSS selectors.
product_cards = soup.select(".card-information, .product-card")

for card in product_cards:
  # Extracting product details safely
  title_elem = card.select_one(".full-unstyled-link, .product-card__title, h3")
  price_elem = card.select_one(".price, .money")
  link_elem = card.select_one("a")

  title = title_elem.get_text(strip=True) if title_elem else "N/A"
  price = price_elem.get_text(strip=True) if price_elem else "N/A"
  
  link = "N/A"
  if link_elem and "href" in link_elem.attrs:
    href = link_elem["href"]
    link = href if href.startswith("http") else "https://shop.mattel.com" + href

  products.append({
      "title": title,
      "price": price,
      "link": link
  })

# Step 4: Store the extracted results in a JSON file
filename = "barbie_products.json"
if products:
  with open(filename, "w", encoding="utf-8") as json_file:
    json.dump(products, json_file, indent=4)
  print(f"Successfully saved {len(products)} products to '{filename}'!")
else:
  print(
      "No products were found. The page structure might rely heavily on"
      " JavaScript, or the CSS selectors need updating."
  )