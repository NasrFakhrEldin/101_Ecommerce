import pytest
from ecommerce.inventory.models import (
    Category,
    Product,
    Brand,
    Media,
    ProductInventory,
    ProductAttribute,
    ProductType,
    ProductAttributeValue,
)


@pytest.fixture
def single_category(db):
    return Category.objects.create(name="default", slug="default")


@pytest.fixture
def category_with_child(db):
    parent = Category.objects.create(name="parent", slug="parent")
    parent.children.create(name="child", slug="child")
    child = parent.children.first()
    return child


@pytest.fixture
def categoty_with_multiple_children(db):
    records = Category.objects.build_tree_nodes(
        {
            "id": 1,
            "name": "parent",
            "slug": "parent",
            "children": [
                {
                    "id": 2,
                    "parent_id": 1,
                    "name": "child",
                    "slug": "child",
                    "children": [
                        {
                            "id": 3,
                            "parent_id": 2,
                            "name": "grandchild",
                            "slug": "grandchild",
                        }
                    ],
                }
            ],
        }
    )
    category = Category.objects.bulk_create(records)
    return category


@pytest.fixture
def single_product(db, category_with_child):
    product = Product.objects.create(
        web_id="123456789",
        name="default",
        slug="default",
        description="default",
        category=category_with_child,
        is_active=True,
    )

    return product


@pytest.fixture
def single_product_attribute(db):
    product_attribute = ProductAttribute.objects.create(
        name="default",
        description="default",
    )
    return product_attribute


@pytest.fixture
def single_product_type(db, single_product_attribute):
    product_type = ProductType.objects.create(
        name="default",
    )
    product_attribute = single_product_attribute
    product_type.product_type_attributes.add(product_attribute)  # add it manually

    return product_type


# @pytest.fixture
# def single_producttypeattribute(db, single_producttype, single_productattribute):
#     producttypeattribute = ProductAttributeValue.objects.create(
#         product_attribute=single_productattribute,
#         product_type=single_producttype,
#     )
#     return producttypeattribute


@pytest.fixture
def single_brand(db):
    brand = Brand.objects.create(name="default")
    return brand


@pytest.fixture
def single_product_attribute_value(db, single_product_attribute):
    product_atrribute_value = ProductAttributeValue.objects.create(
        product_attribute=single_product_attribute,
        attribute_value="default",
    )
    return product_atrribute_value


@pytest.fixture
def single_productinventory(
    db,
    single_product_type,
    single_product,
    single_brand,
    single_product_attribute_value,
):

    product_inventory = ProductInventory.objects.create(
        sku="7633969397",
        upc="100000000001",
        product_type=single_product_type,
        product=single_product,
        brand=single_brand,
        is_active=True,
        is_default=True,
        retail_price="199.99",
        store_price="99.99",
        sale_price="99.99",
        is_on_sale=False,
        is_digital=False,
        weight=1000.0,
    )

    media = Media.objects.create(
        product_inventory=product_inventory,
        img_url="images/default.png",
        alt_text="default",
        is_feature=True,
    )

    product_inventory.attribute_values.add(single_product_attribute_value)

    return {
        "product_inventory": product_inventory,
        "media": media,
        "attribute": single_product_attribute_value,
    }
