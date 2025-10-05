import requests

BASE_URL = "https://hacker-news.firebaseio.com/v0"

def test_first_top_story_happy_path():
    """Happy path: Get first top story details and validate fields"""

    # Step 1: Get list of top stories
    top_stories = requests.get(f"{BASE_URL}/topstories.json").json()
    assert isinstance(top_stories, list)
    assert len(top_stories) > 0

    # Step 2: Take the first story ID
    top_story_id = top_stories[0]

    # Step 3: Fetch its details
    story = requests.get(f"{BASE_URL}/item/{top_story_id}.json").json()

    # Debug prints (commented out for final submission)
    # print("\n--- Happy Path ---")
    # print("Top Story ID:", top_story_id)
    # print("Title:", story.get("title"))
    # print("Author:", story.get("by"))
    # print("Type:", story.get("type"))
    # print("URL:", story.get("url", "N/A"))
    # print("------------------\n")

    # Step 4: Validate important fields
    assert story["id"] == top_story_id
    assert "title" in story
    assert "by" in story
    assert "type" in story and story["type"] == "story"


def test_first_top_story_edge_cases():
    """Edge cases: Ensure story details are valid and safe"""

    response = requests.get(f"{BASE_URL}/topstories.json")
    assert response.status_code == 200, f"❌ Top stories API failed with {response.status_code}"

    try:
        top_stories = response.json()
    except ValueError:
        assert False, "❌ Top stories response is not valid JSON"

    assert isinstance(top_stories, list), "❌ Top stories is not a list"
    assert len(top_stories) > 0, "❌ No stories found"

    top_story_id = top_stories[0]
    story_response = requests.get(f"{BASE_URL}/item/{top_story_id}.json")
    assert story_response.status_code == 200, f"❌ Story API failed with {story_response.status_code}"

    try:
        story = story_response.json()
    except ValueError:
        assert False, "❌ Story response is not valid JSON"

    # Debug prints (commented out for final submission)
    # print("\n--- Edge Case Checks ---")
    # print("Story ID:", story.get("id"))
    # print("Has Title:", "title" in story)
    # print("Has Author:", "by" in story)
    # print("Type:", story.get("type"))
    # print("Has URL:", "url" in story)
    # print("------------------------\n")

    # Edge cases
    assert "id" in story, "❌ Story has no ID"
    assert isinstance(story["id"], int), "❌ Story ID is not an integer"
    assert "title" in story and isinstance(story["title"], str), "❌ Story has no valid title"
    assert "by" in story and isinstance(story["by"], str), "❌ Story has no valid author"

    if "url" in story:
        assert isinstance(story["url"], str), "❌ Story URL is not a string"

    assert story.get("type") == "story", f"❌ Item type is not 'story': {story.get('type')}"

