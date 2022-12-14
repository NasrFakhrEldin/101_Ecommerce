import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

from ecommerce.inventory.models import (
    Category,
    Product,
    ProductType,
    Brand,
    ProductInventory,
    Media,
    Stock,
    ProductAttribute,
    ProductAttributeValue,
    ProductAttributeValues,
)

fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: "cat_name_%d" % n)
    slug = factory.Sequence(lambda n: "cat_slug_%d" % n)
    is_active = True


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    web_id = factory.Sequence(lambda n: "web_id_%d" % n)
    slug = factory.Sequence(lambda n: "pro_slug_%d" % n)
    name = factory.Sequence(lambda n: "pro_name_%d" % n)
    description = fake.text()
    is_active = True
    created_at = "2021-09-04 22:14:18.279092"
    updated_at = "2021-09-04 22:14:18.279092"

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        if extracted:
            for category in extracted:
                self.category.add(category)


class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductType

    name = factory.Sequence(lambda n: "type_%d" % n)


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Sequence(lambda n: "brand_%d" % n)


class ProductInventoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductInventory

    sku = factory.Sequence(lambda n: "sku_%d" % n)
    upc = factory.Sequence(lambda n: "upc_%d" % n)
    product_type = factory.SubFactory(ProductTypeFactory)
    product = factory.SubFactory(ProductFactory)
    brand = factory.SubFactory(BrandFactory)
    is_active = True
    retail_price = 97
    store_price = 92
    sale_price = 46
    weight = 987


class MediaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Media

    product_inventory = factory.SubFactory(ProductInventoryFactory)
    img_url = "images/default.png"
    alt_text = "a default image solid color"
    is_feature = True


class StockFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Stock

    product_inventory = factory.SubFactory(ProductInventoryFactory)
    units = 2
    units_sold = 100


class ProductAttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductAttribute

    name = factory.Sequence(lambda n: "attribute_name_%d" % n)
    description = factory.Sequence(lambda n: "description_%d" % n)


class ProductAttributeValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductAttributeValue

    product_attribute = factory.SubFactory(ProductAttributeFactory)
    attribute_value = factory.Sequence(lambda n: "attribute_value_%d" % n)


class ProductAttributeValuesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductAttributeValues

    attributevalues = factory.SubFactory(ProductAttributeValueFactory)
    productinventory = factory.SubFactory(ProductInventoryFactory)


class ProductWithAttributeValuesFactory(ProductInventoryFactory):
    attributevalues1 = factory.RelatedFactory(
        ProductAttributeValuesFactory,
        factory_related_name="productinventory",
    )
    attributevalues2 = factory.RelatedFactory(
        ProductAttributeValuesFactory,
        factory_related_name="productinventory",
    )


register(CategoryFactory)
register(ProductFactory)
register(ProductTypeFactory)
register(BrandFactory)
register(ProductInventoryFactory)
register(MediaFactory)
register(StockFactory)
register(ProductAttributeFactory)
register(ProductAttributeValueFactory)
register(ProductWithAttributeValuesFactory)
