def test_product_by_category_api(client, single_product):
    product = single_product
    endpoint = f"/dninja/product/{product.category}/"
    response = client().get(endpoint)

    assert response.status_code == 200
