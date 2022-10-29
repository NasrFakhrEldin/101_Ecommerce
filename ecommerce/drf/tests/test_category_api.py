

def test_category_api(api_client, categoty_with_multiple_children):
    endpoint = "/api/v1/category/"

    response = api_client().get(endpoint)
    
    assert response.status_code == 200
    assert len(response.data["results"]) == len(categoty_with_multiple_children)
