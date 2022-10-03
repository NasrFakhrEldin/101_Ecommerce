import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

from ecommerce.inventory.models import Category

fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: "cat_name_%d" % n)
    slug = factory.Sequence(lambda n: "cat_slug_%d" % n)


register(CategoryFactory)
