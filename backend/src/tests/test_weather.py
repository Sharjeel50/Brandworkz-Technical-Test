import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture
def client():
    with TestClient(app, headers={"X-User-Fingerprint": "Test"}) as client:
        yield client


def test_london_weather_response(client: TestClient):
    response = client.get("/weather/current?country=London")
    assert response.status_code == 200
    london_weather_data = response.json()["data"]
    assert london_weather_data["city_name"] == "London"
    assert london_weather_data["country_code"] == "GB"
    assert london_weather_data["state_code"] == "ENG"


def test_incorrect_country_response(client: TestClient):
    response = client.get("/weather/current?country=Germany")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "enum",
                "loc": [
                    "query",
                    "country"
                ],
                "msg": "Input should be 'London', 'New York', 'Mumbai', 'Sydney' or 'Tokyo'",
                "input": "Germany",
                "ctx": {
                    "expected": "'London', 'New York', 'Mumbai', 'Sydney' or 'Tokyo'"
                }
            }
        ]
    }


def test_all_forecast_response(client: TestClient):
    response = client.get("/weather/forecast")
    assert response.status_code == 200
    forecast_data = response.json()["data"]
    cities = [i["city_name"] for i in forecast_data]
    assert cities == ['London', 'New York', 'Mumbai', 'Sydney', 'Tokyo']


def test_single_country_forecast_response(client: TestClient):
    response = client.get("/weather/forecast?country=London")
    assert response.status_code == 200
    forecast_data = response.json()["data"]
    assert forecast_data["city_name"] == "London"
    assert forecast_data["country_code"] == "GB"
    assert forecast_data["state_code"] == "ENG"
    assert len(forecast_data["data"]) == 16


def test_incorrect_country_forecast_response(client: TestClient):
    response = client.get("/weather/forecast?country=Germany")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "enum",
                "loc": [
                    "query",
                    "country"
                ],
                "msg": "Input should be 'London', 'New York', 'Mumbai', 'Sydney' or 'Tokyo'",
                "input": "Germany",
                "ctx": {
                    "expected": "'London', 'New York', 'Mumbai', 'Sydney' or 'Tokyo'"
                }
            }
        ]
    }