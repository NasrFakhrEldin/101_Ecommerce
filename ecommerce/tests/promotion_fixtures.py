from datetime import date, timedelta

import pytest
from ecommerce.promotion.models import Coupon, Promotion, PromoType


@pytest.fixture
def single_promo_type(db):
    promo_type = PromoType.objects.create(
        name="default",
    )
    return promo_type


@pytest.fixture
def single_coupon(db):
    coupon = Coupon.objects.create(
        name="default",
        coupon_code="123456789",
    )
    return coupon


@pytest.fixture
def promotion_with_productinventory(
    db, single_promo_type, single_coupon, single_productinventory
):
    promotion = Promotion.objects.create(
        name="default",
        description="default",
        promo_reduction=50,
        is_active=False,
        is_schedule=True,
        promo_start=date.today(),
        promo_end=date.today() + timedelta(5),
        promo_type=single_promo_type,
        coupon=single_coupon,
    )
    promotion.products_on_promotion.add(
        single_productinventory["product_inventory"],
        through_defaults={"promo_price": "100.00"},
    )
    return promotion
