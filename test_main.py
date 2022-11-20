from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_login():
    response = client.post(
        '/login', json={'login': 'lev', 'password': '12345'})
    assert response.status_code == 200
    data = response.json()
    assert data['status'] == 'authenticated'
