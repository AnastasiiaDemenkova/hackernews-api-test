import requests
import pytest

BASE_URL = "https://hacker-news.firebaseio.com/v0"

# A simple mock response class
class MockResponse:
    def __init__(self, status_code=200, json_data=None):
        self.status_code = status_code
        self._json_data = json_data

    def json(self):
        if self._json_data is None:
            raise ValueError("Invalid JSON")
        return self._json_data


def test_top_stories_api_failure(monkeypatch):
    """Simulate API failure (500 error)"""

    def mock_get(*args, **kwargs):
        return MockResponse(status_code=500)

    monkeypatch.setattr(requests, "get", mock_get)

    response = requests.get(f"{BASE_URL}/topstories.json")
    print("\n--- Simulated API Failure ---")
    print("Status Code Returned:", response.status_code)
    print("-----------------------------\n")

    assert response.status_code == 500, "❌ Expected status code 500"


def test_top_stories_invalid_json(monkeypatch):
    """Simulate invalid JSON in response"""

    def mock_get(*args, **kwargs):
        return MockResponse(status_code=200, json_data=None)  # None → triggers ValueError

    monkeypatch.setattr(requests, "get", mock_get)

    print("\n--- Simulated Invalid JSON ---")
    print("About to raise ValueError because JSON is None")
    print("------------------------------\n")

    with pytest.raises(ValueError):
        response = requests.get(f"{BASE_URL}/topstories.json")
        response.json()


def test_top_stories_empty_list(monkeypatch):
    """Simulate API returning empty list"""

    def mock_get(*args, **kwargs):
        return MockResponse(status_code=200, json_data=[])

    monkeypatch.setattr(requests, "get", mock_get)

    response = requests.get(f"{BASE_URL}/topstories.json")
    data = response.json()

    print("\n--- Simulated Empty List ---")
    print("Data Returned:", data)
    print("Length of list:", len(data))
    print("----------------------------\n")

    assert data == [], "❌ Expected empty list"