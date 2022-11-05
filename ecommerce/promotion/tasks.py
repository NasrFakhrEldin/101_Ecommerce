from datetime import datetime
from decimal import Decimal
from math import ceil

from celery import shared_task
from django.db import transaction
from ecommerce.promotion.models import Promotion


@shared_task()
def promotion_prices(reduction_amount, obj_id):
    with transaction.atomic():
        promotions = Promotion.products_on_promotion.through.objects.filter(
            promotion_id=obj_id
        )
        reduction = reduction_amount / 100

        for promotion in promotions:
            if promotion.price_override == False:
                store_price = promotion.product_inventory_id.store_price
                new_price = ceil(store_price - (store_price * Decimal(reduction)))
                promotion.promo_price = Decimal(new_price)
                promotion.save()


@shared_task()
def promotion_managment_is_active():
    with transaction.atomic():
        promotions = Promotion.objects.filter(is_schedule=True)
        now = datetime.now().date()

        for promotion in promotions:
            if promotion.is_schedule:
                if promotion.promo_end < now:
                    promotion.is_active = False
                    promotion.is_schedule = False
                else:
                    if promotion.promo_start <= now:
                        promotion.is_active = True
                    else:
                        promotion.is_active = False
            promotion.save()
