from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_chunking_logic():
    payload = {
        "text": "This is a sample document for testing chunking. It should work fine.",
        "max_tokens": 100,
    }
    response = client.post("/chunk", json=payload)
    assert response.status_code == 200
    assert "chunks" in response.json()
    assert response.json()["total_chunks"] > 0
    assert response.json()["total_tokens"] > 0
