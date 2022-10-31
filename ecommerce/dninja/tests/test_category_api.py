def test_category_api(c_client, categoty_with_multiple_children):
    endpoint = "/dninja/category/"

    response = c_client().get(endpoint)

    assert response.status_code == 200
    response.content
