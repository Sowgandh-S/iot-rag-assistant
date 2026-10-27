from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_guide_search_endpoint():
    response = client.get(
        "/guide/search",
        params={"question": "What is the temperature range?"},
    )

    assert response.status_code == 200
    result = response.json()
    assert result["found"] is True
    assert result["passages"]
    assert result["source"] == "data/home_sensor_guide.txt"


def test_guide_search_rejects_too_short_question():
    response = client.get("/guide/search", params={"question": "?"})

    assert response.status_code == 422
