# Product Lookup API

## Problem

Businesses often work with product barcodes, inventory lists, or order data. Manually searching product information from a barcode can take time.

This project uses a UPC code to request product information from an external API and saves a simple product report.

## How It Works

The script has a list of products with UPC codes.

For each product, the script:

1. Sends a request to the UPC Item DB API.
2. Passes the UPC code as a request parameter.
3. Checks if the API request was successful.
4. Converts the API response into Python data.
5. Extracts the product title and brand.
6. Saves the result into a JSON report.

## Project Structure

```text
08-product-lookup-api/
├── README.md
├── main.py
├── requirements.txt
├── .gitignore
└── product_lookup_report.json
```

## Setup

Create and activate a virtual environment, then install the required package:

```powershell
pip install -r requirements.txt
```

## How To Run

```powershell
python main.py
```

## Example Output

```text
Product lookup report saved.
```

## Output File

The script creates:

```text
product_lookup_report.json
```

Example report structure:

```json
[
    {
        "label": "Raspberry lemonade",
        "upc": "025000044908",
        "title": "Product title from API",
        "brand": "Product brand from API"
    }
]
```

## What I Learned

In this project, I practiced:

- using an external API
- sending API parameters with `params=`
- using `timeout=10` so the request does not wait forever
- checking `status_code`
- converting API responses into Python dictionaries
- working with nested JSON data
- safely handling missing or failed API responses
- saving API results as a JSON report

## Business Value

This kind of script can help a business enrich product lists automatically. Instead of searching product names and brands by hand, the script can use barcode numbers and create a structured report.
