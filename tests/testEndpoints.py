from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_valid_endpoint_cot():
    response = client.get("/cot")
    assert response.status_code == 200


def test_valid_endpoint_cotacao():
    response = client.get("/cotacao")
    assert response.status_code == 200


def test_valid_endpoint_name():
    response = client.get("/hello/Fabio")
    assert response.status_code == 200
