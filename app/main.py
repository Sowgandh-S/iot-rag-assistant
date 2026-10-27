from fastapi import FastAPI, Query

from app.retrieval import retrieve_passages
from app.sensor_data import summarize_location

app = FastAPI(
    title="IoT Home Sensor Assistant",
    description="A learning API for sample home sensor data and guide search.",
    version="0.2.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/sensors/{location}/summary")
def get_sensor_summary(location: str):
    return summarize_location(location)


@app.get("/guide/search")
def search_guide(
    question: str = Query(..., min_length=2, description="Question to search for"),
):
    passages = retrieve_passages(question)

    return {
        "question": question,
        "source": "data/home_sensor_guide.txt",
        "passages": passages,
        "found": bool(passages),
    }
