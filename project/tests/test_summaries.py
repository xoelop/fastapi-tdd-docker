def test_create_summary(test_app_with_db):
    response = test_app_with_db.post("/summaries/", json={"url": "https://foo.bar"})

    assert response.status_code == 201
    assert response.json()["url"] == "https://foo.bar"


def test_create_summaries_invalid_json(test_app_with_db):
    response = test_app_with_db.post("/summaries/", json={})
    assert not response.ok


def test_read_summary(test_app_with_db):
    create_response = test_app_with_db.post(
        "/summaries/", json={"url": "https://test.url"}
    )
    create_response_id = create_response.json()["id"]
    assert create_response.ok

    get_response = test_app_with_db.get(f"/summaries/{create_response_id}")
    assert get_response.ok

    assert create_response.json()["id"] == get_response.json()["id"]
    assert create_response.json()["url"] == get_response.json()["url"]
    assert get_response.json()["summary"]
    assert get_response.json()["created_at"]


def test_get_all_summaries(test_app_with_db):

    test_app_with_db.post("/summaries/", json={"url": "https://test.url"})
    test_app_with_db.post("/summaries/", json={"url": "https://test.url"})
    test_app_with_db.post("/summaries/", json={"url": "https://test.url"})

    response = test_app_with_db.get("/summaries/")
    assert response.ok
    assert len(response.json()) > 0
