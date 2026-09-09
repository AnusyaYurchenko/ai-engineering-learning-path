# Weather API Report

## Problem

Businesses sometimes need quick weather information for travel planning, delivery planning, events, or daily operations.

This project uses the OpenWeather API to get a short forecast for a city and saves the result as a structured JSON report.

## How It Works

The script:

1. Loads the OpenWeather API key from `.env`.
2. Sends a request to the OpenWeather forecast API.
3. Passes the city, country code, API key, and units as request parameters.
4. Checks if the API request was successful.
5. Converts the API response into Python data.
6. Extracts a small forecast summary.
7. Saves the result into `weather_report.json`.

## Project Structure

```text
09-weather-api-report/
├── README.md
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── weather_report.json
```

## Setup

Create a `.env` file and add your real OpenWeather API key:

```text
OPENWEATHER_API_KEY=your_real_api_key_here
```

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
Weather report saved to weather_report.json.
```

## Output File

The script creates:

```text
weather_report.json
```

Example report structure:

```json
{
    "location": "Paris, FR",
    "forecast": [
        {
            "date_time": "2026-09-09 12:00:00",
            "temperature_celsius": 18.5,
            "weather": "light rain"
        }
    ]
}
```

## What I Learned

In this project, I practiced:

- using an external API
- protecting API keys with `.env`
- loading environment variables with `python-dotenv`
- sending request parameters with `params=`
- using `timeout=10` for safer API calls
- checking API response status codes
- converting API responses into Python dictionaries
- reading nested JSON data
- using `.get()` fallback values
- saving API data as a JSON report

## Business Value

This type of script can help a business collect weather information automatically instead of checking it manually. It could later be expanded for delivery planning, event planning, or travel reports.
