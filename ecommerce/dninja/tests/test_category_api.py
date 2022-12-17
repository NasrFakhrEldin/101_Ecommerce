def test_category_api(client, categoty_with_multiple_children):
    endpoint = "/dninja/category/"

    response = client().get(endpoint)

    assert response.status_code == 200
    response.content
