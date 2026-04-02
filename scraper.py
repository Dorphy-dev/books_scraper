import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_rating(star_class):
    ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return ratings.get(star_class, 0)

def scrape_page(page):
    url = BASE_URL.format(page)
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    data = []

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        availability = book.find("p", class_="instock availability").text.strip()
        rating_class = book.find("p", class_="star-rating")["class"][1]

        data.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": get_rating(rating_class)
        })

    return data
