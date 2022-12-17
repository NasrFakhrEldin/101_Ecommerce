import pytest
from ecommerce.drf.utils import convert_to_dot_notation
from ecommerce.inventory.models import (
    Brand,
    Product,
    ProductAttribute,
    ProductAttributeValue,
    ProductInventory,
    ProductType,
)


@pytest.fixture
def three_product(db, single_category):
    first_product = Product.objects.create(
        web_id="45425810",
        name="default",
        slug="default",
        description="default",
        category=single_category,
        is_active=True,
    )
    second_product = Product.objects.create(
        web_id="45425811",
        name="default",
        slug="default",
        description="default",
        category=single_category,
        is_active=True,
    )
    third_product = Product.objects.create(
        web_id="45425812",
        name="default",
        slug="default",
        description="default",
        category=single_category,
        is_active=True,
    )
    return {
        "first_product": first_product,
        "second_product": second_product,
        "third_product": third_product,
    }


@pytest.fixture
def three_product_attribute(db):
    first_product_attribute = ProductAttribute.objects.create(
        name="name1",
        description="first_default",
    )
    second_product_attribute = ProductAttribute.objects.create(
        name="name2",
        description="second_default",
    )
    third_product_attribute = ProductAttribute.objects.create(
        name="name3",
        description="third_default",
    )
    return {
        "first_product_attribute": first_product_attribute,
        "second_product_attribute": second_product_attribute,
        "third_product_attribute": third_product_attribute,
    }


@pytest.fixture
def three_product_type(db, three_product_attribute):
    data = convert_to_dot_notation(three_product_attribute)

    first_product_type = ProductType.objects.create(
        name="first_default",
    )
    first_product_type.product_type_attributes.add(data.first_product_attribute)

    second_product_type = ProductType.objects.create(
        name="second_default",
    )
    second_product_type.product_type_attributes.add(data.second_product_attribute)

    third_product_type = ProductType.objects.create(
        name="third_default",
    )
    third_product_type.product_type_attributes.add(data.third_product_attribute)

    return {
        "first_product_type": first_product_type,
        "second_product_type": second_product_type,
        "third_product_type": third_product_type,
    }


@pytest.fixture
def three_brand(db):
    first_brand = Brand.objects.create(name="first_default")
    second_brand = Brand.objects.create(name="second_default")
    third_brand = Brand.objects.create(name="third_default")
    return {
        "first_brand": first_brand,
        "second_brand": second_brand,
        "third_brand": third_brand,
    }


@pytest.fixture
def three_product_attribute_value(db, three_product_attribute):
    data = convert_to_dot_notation(three_product_attribute)

    first_attribute_value = ProductAttributeValue.objects.create(
        product_attribute=data.first_product_attribute,
        attribute_value="default",
    )

    second_attribute_value = ProductAttributeValue.objects.create(
        product_attribute=data.second_product_attribute,
        attribute_value="default",
    )
    third_attribute_value = ProductAttributeValue.objects.create(
        product_attribute=data.third_product_attribute,
        attribute_value="default",
    )
    return {
        "first_attribute_value": first_attribute_value,
        "second_attribute_value": second_attribute_value,
        "third_attribute_value": third_attribute_value,
    }


@pytest.fixture
def create_three_productinventory(
    db,
    three_product_type,
    three_product,
    three_brand,
    three_product_attribute_value,
):
    types = convert_to_dot_notation(three_product_type)
    products = convert_to_dot_notation(three_product)
    brands = convert_to_dot_notation(three_brand)
    attributes = convert_to_dot_notation(three_product_attribute_value)

    first_product_inventory = ProductInventory.objects.create(
        sku="7633969397",
        upc="100000000001",
        product_type=types.first_product_type,
        product=products.first_product,
        brand=brands.first_brand,
        is_active=True,
        is_default=True,
        retail_price="97",
        store_price="92",
        sale_price="46",
        is_on_sale=False,
        is_digital=False,
        weight=1000.0,
    )
    second_product_inventory = ProductInventory.objects.create(
        sku="6327000212",
        upc="100000000002",
        product_type=types.second_product_type,
        product=products.second_product,
        brand=brands.second_brand,
        is_active=True,
        is_default=True,
        retail_price="99",
        store_price="94",
        sale_price="47",
        is_on_sale=False,
        is_digital=False,
        weight=1000.0,
    )
    third_product_inventory = ProductInventory.objects.create(
        sku="7763166969",
        upc="100000000003",
        product_type=types.third_product_type,
        product=products.third_product,
        brand=brands.third_brand,
        is_active=True,
        is_default=True,
        retail_price="88",
        store_price="84",
        sale_price="42",
        is_on_sale=False,
        is_digital=False,
        weight=1000.0,
    )

    first_product_inventory.attribute_values.add(attributes.first_attribute_value)
    second_product_inventory.attribute_values.add(attributes.second_attribute_value)
    third_product_inventory.attribute_values.add(attributes.third_attribute_value)

    return {
        "first_product": first_product_inventory,
        "second_product": second_product_inventory,
        "third_product": third_product_inventory,
    }
