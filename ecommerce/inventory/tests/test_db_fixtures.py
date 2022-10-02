import pytest
from ecommerce.inventory.models import Category


# # @pytest.mark.dbfixture
# @pytest.mark.parametrize(
#     "id, name, slug, is_active",
#     [
#         (1, "fashion", "fashion", 1),
#         # (3, "trainers", "trainers", 1),
#         # (5, "baseball", "baseball", 1),
#     ],
# )
# def test_inventory_category_dbfixture(db, db_fixture_setup, id, name, slug, is_active):

#     result = Category.objects.get(id=id)
#     print(result.name)
#     assert result.name == name
#     assert result.slug == slug
#     assert result.is_active == is_active


@pytest.mark.parametrize(
    "name, slug, is_active",
    [
        ("fashion", "fashion", 1),
        ("trainers", "trainers", 1),
        ("baseball", "baseball", 1),
    ],
)
def test_inventory_db_category_insert_data(db, db_fixture_setup, name, slug, is_active):

    result = Category.objects.create(name=name, slug=slug, is_active=is_active)
    print(result.name)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.parametrize(
    "is_active",
    [
        (1),
        (1),
        (1),
    ],
)
def test_inventory_db_category_insert_data_(db, category_factory, is_active):

    result = category_factory.create(is_active=is_active)
    print(result.name)
    assert result.is_active == is_active
