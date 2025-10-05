# HackerNews API Test Suite

Automated acceptance tests for the public [HackerNews API](https://github.com/HackerNews/API).

## Overview

This project verifies the functionality and robustness of key HackerNews endpoints:

- **Top Stories**: Retrieve a list of top story IDs.
- **First Top Story Details**: Fetch details for the first top story.
- **First Comment**: Retrieve the first comment from the first top story.

Each test case includes:
- **Happy path** validation
- **Edge case** handling
- **Mocked failure simulations** (API error, invalid JSON, empty list)

---

## Setup

1. **Clone the repository**
   ```sh
   git clone https://github.com/<your-username>/hackernews-api-test.git
   cd hackernews-api-test
   ```

2. **Create and activate a virtual environment**
   ```sh
   python3 -m venv venv
   source venv/bin/activate   # Mac/Linux
   # venv\Scripts\activate    # Windows
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

---

## Running Tests

- **Run all tests**
  ```sh
  pytest -s tests
  ```

- **Run a specific test file**
  ```sh
  pytest -s tests/test_top_stories.py
  pytest -s tests/test_first_top_story_details.py
  pytest -s tests/test_first_comment.py
  ```

- **Run a specific test**
  ```sh
  pytest -s tests/test_first_comment.py::test_first_comment_happy_path
  ```

---

## Project Structure

```
hackernews-api-test/
│
├── tests/
│   ├── test_top_stories.py             # Test Case 1: Top Stories API
│   ├── test_first_top_story_details.py # Test Case 2: First Story Details
│   ├── test_first_comment.py           # Test Case 3: First Comment
│   └── test_top_stories_mocks.py       # Bonus: Mocked failure simulations
│
├── requirements.txt                    # Dependencies
├── README.md                           # Setup & run instructions
└── .gitignore                          # Ignore venv and cache files
```

---

## Test Coverage

### 1. Top Stories API
- **Happy path**: Returns a non-empty list of story IDs.
- **Edge cases**: API response validation (status code, JSON format, integer IDs).

### 2. First Top Story Details
- **Happy path**: Story has `id`, `title`, `by`, and `type="story"`.
- **Edge cases**: Missing/malformed fields, incorrect type.

### 3. First Comment
- **Happy path**: First comment exists with `id`, `by`, `text`, `type="comment"`.
- **Edge cases**: No comments, deleted/empty comment handling.

### 4. Bonus: Mocked Tests
- Simulated API failure (500)
- Simulated invalid JSON
- Simulated empty list

---

## Notes

- All tests currently pass against the live HackerNews API.
- For debugging, you can uncomment `print()` statements inside the tests to inspect IDs, authors, and text.
- Some HackerNews stories may not have a `url` (e.g., Ask HN posts) — tests account for this.
- Some stories may not have comments - this is considered an acceptable edge case outcome.

## Reflections

- **Easy**: Writing happy path tests with `requests` and `pytest` was straightforward.  
- **Hard**: Handling optional fields (`url`, missing comments) required thinking about realistic edge cases.  
- **Interesting**: Simulating failure scenarios with mocked responses showed how tests behave when APIs misbehave.  