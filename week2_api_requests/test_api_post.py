import requests

def test_create_post():
    url = 'https://jsonplaceholder.typicode.com/posts'
    payload = {
        "title" : "QA Automation Journey",
        "body": "Learning POST request with pytest",
        "userId": 101
    }

    response = requests.post(url, json=payload)
    data = response.json()

    assert response.status_code == 201, "Expected status code 201"
    assert data["title"] == payload["title"], "title mismatch"
    assert data["body"] == payload["body"], "body mismatch"
    assert data["userId"] == payload["userId"], "UserId mismatch"

