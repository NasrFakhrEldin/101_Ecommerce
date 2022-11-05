from datetime import date, timedelta

import pytest
from ecommerce.promotion.models import Promotion
from ecommerce.promotion.tasks import promotion_managment_is_active, promotion_prices


@pytest.mark.parametrize(
    "reduction, store_price_result",
    [(10, 90), (50, 50)],
)
def test_promotion_action(
    reduction,
    store_price_result,
    celery_app,
    celery_worker,
    promotion_with_productinventory,
):
    promotion_prices(reduction, promotion_with_productinventory.id)
    new_price = Promotion.products_on_promotion.through.objects.get(
        promotion_id=promotion_with_productinventory.id
    )
    assert new_price.promo_price == store_price_result


@pytest.mark.parametrize(
    "promo_start, promo_end, result",
    [
        (date.today(), date.today() + timedelta(5), True),
        (date.today() + timedelta(5), date.today() + timedelta(10), False),
        (date.today() - timedelta(10), date.today() - timedelta(5), False),
    ],
)
def test_promotion_managment_is_active(
    promo_start,
    promo_end,
    result,
    celery_app,
    celery_worker,
    promotion_with_productinventory,
):
    promotion_with_productinventory.promo_start = promo_start
    promotion_with_productinventory.promo_end = promo_end
    promotion_with_productinventory.save(update_fields=["promo_start", "promo_end"])
    promotion_managment_is_active()

    promotion = Promotion.objects.all().first()

    assert promotion.is_active == result
