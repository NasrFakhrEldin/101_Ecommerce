from ecommerce.inventory.models import Product


def test_create_single_product_with_sub_category(single_product):
    new_product = single_product
    get_product = Product.objects.all().first()

    assert new_product.id == get_product.id
    assert new_product.web_id == get_product.web_id
    assert new_product.name == get_product.name
    assert new_product.slug == get_product.slug
    assert new_product.description == get_product.description
    assert new_product.category == get_product.category
    assert new_product.is_active == get_product.is_active

    print(new_product.name)
    print(get_product.category.name)
