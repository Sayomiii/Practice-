import json
from bs4 import BeautifulSoup
import requests


url = "http://books.toscrape.com/"

print("Fetching books page...")
response = requests.get(url, timeout=10)
response.raise_for_status()


soup = BeautifulSoup(response.text, "html.parser")
books = []


product_cards = soup.select("article.product_pod")

for card in product_cards:
  title = card.h3.a["title"]
  price = card.select_one("p.price_color").text
  availability = card.select_one("p.instock.availability").text.strip()
  link = "http://books.toscrape.com/" + card.h3.a["href"]

  books.append({
      "title": title,
      "price": price,
      "availability": availability,
      "link": link,
  })


filename = "scraped_books.json"
with open(filename, "w", encoding="utf-8") as json_file:
  json.dump(books, json_file, indent=4)

print(f"Successfully saved {len(books)} books to '{filename}'!")
