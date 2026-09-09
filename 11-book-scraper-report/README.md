# Book Scraper Report

## Problem

Businesses sometimes need to collect public information from websites and turn it into structured reports.

This project scrapes book data from a safe practice website and saves the results as JSON and CSV reports.

## How It Works

The script visits multiple pages from `books.toscrape.com`.

For each page, it:

1. Sends a request to get the webpage HTML.
2. Checks if the request was successful.
3. Parses the HTML with BeautifulSoup.
4. Finds book cards on the page.
5. Extracts each book title, price, availability, and rating.
6. Saves the collected data into JSON and CSV files.

## Project Structure

```text
11-book-scraper-report/
├── README.md
├── main.py
├── requirements.txt
├── .gitignore
├── books_report.json
└── books_report.csv
```

## Setup

Install the required packages:

```powershell
pip install -r requirements.txt
```

## How To Run

```powershell
python main.py
```

## Example Output

```text
Page 1 scraped: 20 books found.
Page 2 scraped: 20 books found.
Page 3 scraped: 20 books found.
Book reports saved.
```

## Output Files

The script creates two report files:

```text
books_report.json
books_report.csv
```

Example JSON item:

```json
{
    "page": 1,
    "title": "A Light in the Attic",
    "price": "51.77",
    "availability": "In stock",
    "rating": "Three"
}
```

## What I Learned

In this project, I practiced:

- sending webpage requests with `requests`
- using `timeout=10` for safer requests
- parsing HTML with BeautifulSoup
- finding elements with CSS selectors
- extracting text from HTML elements
- cleaning text with `.strip()`
- collecting scraped data into dictionaries
- saving scraped data as JSON
- saving scraped data as CSV
- using `sleep()` between page requests

## Business Value

This type of script can help a business collect public website data and turn it into a structured report. It can be useful for market research, product monitoring, competitor research, or internal reporting.

## Note

This project uses a practice website made for scraping exercises. Real websites may have rules against scraping, so it is important to check a website's terms before using scraping in real business work.
