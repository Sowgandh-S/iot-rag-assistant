import csv
from pathlib import Path


DEFAULT_CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "sample_readings.csv"


def load_readings(csv_path: Path = DEFAULT_CSV_PATH) -> list[dict]:
    """Load fictional sensor readings from a CSV file."""
    with csv_path.open(newline="", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))


def summarize_location(location: str, csv_path: Path = DEFAULT_CSV_PATH) -> dict:
    """Return basic temperature and humidity summaries for one home location."""
    readings = [
        row for row in load_readings(csv_path)
        if row["location"] == location
    ]

    if not readings:
        return {"location": location, "count": 0}

    temperatures = [float(row["temperature_c"]) for row in readings]
    humidities = [float(row["humidity_percent"]) for row in readings]

    return {
        "location": location,
        "count": len(readings),
        "average_temperature_c": round(sum(temperatures) / len(temperatures), 1),
        "minimum_temperature_c": min(temperatures),
        "maximum_temperature_c": max(temperatures),
        "average_humidity_percent": round(sum(humidities) / len(humidities), 1),
    }
