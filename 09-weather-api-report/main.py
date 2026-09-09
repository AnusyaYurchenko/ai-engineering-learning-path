import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.getenv("OPENWEATHER_API_KEY")


CITY = "Paris"
COUNTRY_CODE = "FR"
REPORT_FILE = "weather_report.json"


def get_weather_data(city, country_code, api_key):
    parameters = {
        "q": f"{city},{country_code}",
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=parameters, timeout=10)
    except requests.RequestException:
        return None

    if response.status_code != 200:
        return None

    try:
        return response.json()
    except ValueError:
        return None


def create_forecast_summary(weather_data, limit=5):
    forecast_items = weather_data.get("list", [])[:limit]
    summary = []

    for item in forecast_items:
        weather = item.get("weather", [{}])[0]
        main = item.get("main", {})

        summary.append({
            "date_time": item.get("dt_txt", "Unknown time"),
            "temperature_celsius": main.get("temp", "Unknown temperature"),
            "weather": weather.get("description", "Unknown weather")
        })

    return summary


def create_weather_report(city, country_code, weather_data):
    return {
        "location": f"{city}, {country_code}",
        "forecast": create_forecast_summary(weather_data)
    }


def save_json_report(file_name, report):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)


def main():
    if not API_KEY:
        print("OpenWeather API key is missing.")
        return

    weather_data = get_weather_data(CITY, COUNTRY_CODE, API_KEY)

    if not weather_data:
        print("Could not get weather data.")
        return

    report = create_weather_report(CITY, COUNTRY_CODE, weather_data)
    save_json_report(REPORT_FILE, report)

    print(f"Weather report saved to {REPORT_FILE}.")


if __name__ == "__main__":
    main()
