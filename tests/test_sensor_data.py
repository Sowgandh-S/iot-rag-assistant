from pathlib import Path

from app.sensor_data import load_readings, summarize_location


def test_load_readings_returns_all_rows():
    readings = load_readings()

    assert len(readings) == 5
    assert readings[0]["location"] == "living_room"


def test_summarize_living_room():
    summary = summarize_location("living_room")

    assert summary["count"] == 3
    assert summary["minimum_temperature_c"] == 27.8
    assert summary["maximum_temperature_c"] == 30.4
    assert summary["average_humidity_percent"] == 40.3


def test_unknown_location_returns_zero_readings():
    summary = summarize_location("garage")

    assert summary == {"location": "garage", "count": 0}
