import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_index_returns_html(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"Book Inventory" in res.data

def test_health_response(client):
    res = client.get("/health")
    data = res.get_json()
    assert res.status_code == 200
    assert data["status"] == "healthy"
    assert data["total_books"] == 5
    assert data["available_books"] == 3

def test_get_books_response(client):
    res = client.get("/api/books")
    data = res.get_json()
    assert res.status_code == 200
    assert data["count"] == 5
    assert len(data["books"]) == 5
