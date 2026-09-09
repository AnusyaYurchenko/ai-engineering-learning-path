import json
import requests

BASE_URL = "https://api.upcitemdb.com/prod/trial/lookup"

PRODUCTS = [
    {"upc": "025000044908", "label": "Raspberry lemonade"},
    {"upc": "028400516686", "label": "Ridged potato chips"}
]


def get_product_data(upc):
    parameters = {"upc": upc}

    try:
        response = requests.get(BASE_URL, params=parameters, timeout=10)
    except requests.RequestException:
        return None

    if response.status_code != 200:
        return None

    try:
        data = response.json()
    except ValueError:
        return None

    items = data.get("items", [])

    if not items:
        return None

    item = items[0]

    return {
        "upc": upc,
        "title": item.get("title", "Unknown title"),
        "brand": item.get("brand", "Unknown brand")
    }


def create_product_report(products):
    report = []

    for product in products:
        product_data = get_product_data(product["upc"])

        if product_data:
            report.append({
                "label": product["label"],
                "upc": product_data["upc"],
                "title": product_data["title"],
                "brand": product_data["brand"]
            })
        else:
            report.append({
                "label": product["label"],
                "upc": product["upc"],
                "title": "Not found",
                "brand": "Not found"
            })

    return report


def save_json_report(file_name, report):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)


def main():
    report = create_product_report(PRODUCTS)
    save_json_report("product_lookup_report.json", report)

    print("Product lookup report saved.")


if __name__ == "__main__":
    main()
