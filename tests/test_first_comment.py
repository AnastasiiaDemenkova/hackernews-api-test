import requests

BASE_URL = "https://hacker-news.firebaseio.com/v0"

def test_first_comment_happy_path():
    """Happy path: Get the first top story's first comment"""

    # Step 1: Get top stories
    top_stories = requests.get(f"{BASE_URL}/topstories.json").json()
    assert isinstance(top_stories, list)
    assert len(top_stories) > 0

    # Step 2: Get first top story details
    top_story_id = top_stories[0]
    story = requests.get(f"{BASE_URL}/item/{top_story_id}.json").json()

    # Step 3: Ensure story has comments
    assert "kids" in story and isinstance(story["kids"], list), "❌ Story has no comments list"
    assert len(story["kids"]) > 0, "❌ Story has no comments"

    first_comment_id = story["kids"][0]

    # Step 4: Get first comment details
    comment = requests.get(f"{BASE_URL}/item/{first_comment_id}.json").json()

    # Debug prints (commented out for submission)
    # print("\n--- Happy Path ---")
    # print("Top Story ID:", top_story_id)
    # print("First Comment ID:", first_comment_id)
    # print("Comment Author:", comment.get("by"))
    # print("Comment Text:", comment.get("text"))
    # print("------------------\n")

    # Step 5: Validate comment fields
    assert comment["id"] == first_comment_id
    assert "by" in comment
    assert "text" in comment
    assert comment.get("type") == "comment"


def test_first_comment_edge_cases():
    """Edge cases: Ensure comment fetching is safe"""

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

    # Edge case: story has no kids/comments
    if "kids" not in story or len(story["kids"]) == 0:
        # print("\n--- Edge Case ---")
        # print("Story ID:", story.get("id"))
        # print("No comments available for this story.")
        # print("-----------------\n")
        assert True  # acceptable outcome
        return

    # Edge case: first comment fetch
    first_comment_id = story["kids"][0]
    comment_response = requests.get(f"{BASE_URL}/item/{first_comment_id}.json")
    assert comment_response.status_code == 200, f"❌ Comment API failed with {comment_response.status_code}"

    try:
        comment = comment_response.json()
    except ValueError:
        assert False, "❌ Comment response is not valid JSON"

    # print("\n--- Edge Case Checks ---")
    # print("First Comment ID:", first_comment_id)
    # print("Has ID:", "id" in comment)
    # print("Has Author:", "by" in comment)
    # print("Has Text:", "text" in comment)
    # print("Type:", comment.get("type"))
    # print("-------------------------\n")

    # Validations
    assert "id" in comment, "❌ Comment has no ID"
    assert isinstance(comment["id"], int), "❌ Comment ID is not an integer"
    assert comment.get("type") == "comment", f"❌ Item is not a comment: {comment.get('type')}"

    if "text" in comment:
        assert isinstance(comment["text"], str), "❌ Comment text is not a string"