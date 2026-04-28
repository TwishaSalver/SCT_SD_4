import requests
from bs4 import BeautifulSoup
import csv

URL = "http://books.toscrape.com/"

def get_page(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")

def extract_books(soup):
    books = soup.find_all("article", class_="product_pod")
    data = []

    for book in books:
        name = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.find("p", class_="star-rating")["class"][1]

        data.append({
            "Name": name,
            "Price": price,
            "Rating": rating
        })

    return data

def save_to_csv(data, filename="books.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Price", "Rating"])
        writer.writeheader()
        writer.writerows(data)

def main():
    soup = get_page(URL)
    books = extract_books(soup)
    save_to_csv(books)

    print("✅ Data saved to books.csv")

if __name__ == "__main__":
    main()