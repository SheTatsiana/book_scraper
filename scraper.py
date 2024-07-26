
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "http://books.toscrape.com/"
response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    books = []

    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        books.append({
            'Title': title,
            'Price': price
        })

    df = pd.DataFrame(books)
    df.to_csv('books.csv', index=False)
    print("Data has been written to books.csv")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
