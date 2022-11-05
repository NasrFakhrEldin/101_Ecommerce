pytest_plugins = [
    "ecommerce.tests.c_client",
    "ecommerce.tests.inventory_fixtures",
    "ecommerce.tests.api_client",
    "ecommerce.tests.fixtures",
    "ecommerce.tests.selenium",
    "ecommerce.tests.factories",
    "ecommerce.tests.promotion_fixtures",
    "celery.contrib.pytest",
]
