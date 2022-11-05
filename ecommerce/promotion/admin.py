from django.contrib import admin
from ecommerce.promotion import models
from ecommerce.promotion.tasks import promotion_managment_is_active, promotion_prices


class ProductsOnPromotion(admin.StackedInline):
    model = models.Promotion.products_on_promotion.through
    extra = 1
    raw_id_fields = ("product_inventory_id",)


@admin.register(
    models.Promotion,
)
class ProductInventoryList(admin.ModelAdmin):
    model = models.Promotion
    list_display = ("name", "is_active", "promo_reduction", "promo_start", "promo_end")
    inlines = (ProductsOnPromotion,)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        promotion_prices.delay(obj.promo_reduction, obj.id)
        promotion_managment_is_active.delay()


admin.site.register(models.PromoType)
admin.site.register(models.Coupon)
