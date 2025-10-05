import requests

BASE_URL = "https://hacker-news.firebaseio.com/v0"

def test_top_stories_happy_path():
    """Check that Top Stories API works under normal conditions"""
    response = requests.get(f"{BASE_URL}/topstories.json")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert all(isinstance(i, int) for i in data)
    
    # Debug prints (commented out for final submission)
    # print("\n--- Happy Path ---")
    # print("✅ Number of top stories returned:", len(data))
    # print("✅ First top story ID:", data[0])
    # print("✅ First 5 top story IDs:", data[:5])
    # print("------------------\n")


def test_top_stories_edge_cases():
    """Check possible edge cases for Top Stories API"""
    response = requests.get(f"{BASE_URL}/topstories.json")
    
    # Edge case: API failure
    assert response.status_code == 200, f"❌ API failed with status code {response.status_code}"
    
    try:
        data = response.json()
    except ValueError:
        assert False, "❌ Response is not valid JSON"
    
    # Edge case: Not a list
    assert isinstance(data, list), "❌ Top stories is not a list"
    
    # Edge case: Empty list
    assert len(data) > 0, "❌ Top stories list is empty"
    
    # Edge case: IDs not integers
    assert all(isinstance(i, int) for i in data), "❌ Some top story IDs are not integers"
    
    # Debug prints (commented out for final submission)
    # print("\n--- Edge Cases ---")
    # print("✅ Data type:", type(data))
    # print("✅ Length of list:", len(data))
    # print("------------------\n")