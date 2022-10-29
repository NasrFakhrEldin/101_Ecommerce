from utils import convert_to_dot_notation
import json


def test_product_by_category_api(api_client, single_product):
    product = single_product
    endpoint = f"/api/v1/product/{product.category}/"
    response = api_client().get(endpoint)

    expected_json = [{"name": product.name, "web_id": product.web_id}]

    assert response.status_code == 200
    assert response.data == expected_json


def test_productinventory_api(api_client, single_productinventory):
    fixture = convert_to_dot_notation(single_productinventory)

    endpoint = f"/api/v1/product-inventory/{fixture.product_inventory.product.web_id}/"
    response = api_client().get(endpoint)

    expected_json = [
        {
            "id": fixture.product_inventory.id,
            "sku": fixture.product_inventory.sku,
            "store_price": fixture.product_inventory.store_price,
            "is_default": fixture.product_inventory.is_default,
            "brand": {"name": fixture.product_inventory.brand.name},
            "product": {
                "name": fixture.product_inventory.product.name,
                "web_id": fixture.product_inventory.product.web_id,
            },
            "is_on_sale": fixture.product_inventory.is_on_sale,
            "weight": fixture.product_inventory.weight,
            "media": [
                {
                    "img_url": fixture.media.img_url.url,
                    "alt_text": fixture.media.alt_text,
                }
            ],
            "attributes": [
                {
                    "attribute_value": fixture.attribute.attribute_value,
                    "product_attribute": {
                        "id": fixture.attribute.id,
                        "name": fixture.attribute.product_attribute.name,
                        "description": fixture.attribute.product_attribute.description,
                    },
                }
            ],
            "product_type": fixture.product_inventory.product_type.id,
        }
    ]

    assert response.status_code == 200
    assert json.loads(response.content) == expected_json
