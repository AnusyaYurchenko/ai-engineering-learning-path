import csv
import json
from time import sleep

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
HEADERS = {"Accept": "text/html", "User-Agent": "Mozilla/5.0"}
PAGES_TO_SCRAPE = 3


def get_page_html(page_number):
    url = BASE_URL.format(page_number)

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
    except requests.RequestException:
        return None

    if response.status_code != 200:
        return None

    return response.text


def clean_price(price_element):
    if not price_element:
        return "Unknown price"

    return price_element.get_text(strip=True).replace("Â", "").replace("£", "")


def get_book_rating(rating_classes):
    possible_ratings = ["One", "Two", "Three", "Four", "Five"]

    for rating in possible_ratings:
        if rating in rating_classes:
            return rating

    return "Unknown"


def extract_books_from_html(html, page_number):
    parsed_page = BeautifulSoup(html, "html.parser")
    book_cards = parsed_page.select("article.product_pod")
    books = []

    for card in book_cards:
        title_element = card.select_one("h3 a")
        price_element = card.select_one(".price_color")
        availability_element = card.select_one(".availability")
        rating_element = card.select_one("p.star-rating")

        if not title_element:
            continue

        rating_classes = rating_element.get("class", []) if rating_element else []

        books.append({
            "page": page_number,
            "title": title_element.get("title", "Unknown title").strip(),
            "price": clean_price(price_element),
            "availability": availability_element.get_text(strip=True) if availability_element else "Unknown availability",
            "rating": get_book_rating(rating_classes)
        })

    return books


def scrape_books(total_pages):
    all_books = []

    for page_number in range(1, total_pages + 1):
        html = get_page_html(page_number)

        if not html:
            print(f"Could not scrape page {page_number}.")
            continue

        books = extract_books_from_html(html, page_number)
        all_books.extend(books)

        print(f"Page {page_number} scraped: {len(books)} books found.")
        sleep(1)

    return all_books


def save_json_report(file_name, books):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4)


def save_csv_report(file_name, books):
    fieldnames = ["page", "title", "price", "availability", "rating"]

    with open(file_name, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)


def main():
    books = scrape_books(PAGES_TO_SCRAPE)

    if not books:
        print("No books were collected.")
        return

    save_json_report("books_report.json", books)
    save_csv_report("books_report.csv", books)

    print("Book reports saved.")


if __name__ == "__main__":
    main()
