import requests
import bs4 as beautifulsoup4
import json

#Websiteurl
url= "https://books.toscrape.com/"

#Getting the website
response = requests.get(url, timeout=20)
response.raise_for_status()
print(response.content)

#Parsing the response content using BeautifulSoup
soup = beautifulsoup4.BeautifulSoup(response.content, 'html.parser')

#An empty list to store the book data
books = []
for article in soup.find_all('article', class_='product_pod'):
    title = article.h3.a['title']
    price = article.find('p', class_='price_color').text
    rating = article.find('p', class_='star-rating')['class'][1]
    availability = article.find('p', class_='instock availability').text.strip()
    
    # Appending the book data to the list
    books.append({
        'title': title,
        'price': price,
        'rating': rating,
        'availability': availability
    })

# Saving the book data to a JSON file
with open('books.json', 'w', encoding='utf-8') as file:
    json.dump(books, file, indent=4, ensure_ascii=False)
print("I have successfully scraped the book data and saved it to books.json")
