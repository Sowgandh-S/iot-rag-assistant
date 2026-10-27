from fastapi import FastAPI

from app.sensor_data import summarize_location

app = FastAPI(
    title="IoT Home Sensor Assistant",
    description="An educational API for summarizing fictional home sensor readings.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/sensors/{location}/summary")
def get_sensor_summary(location: str):
    return summarize_location(location)
