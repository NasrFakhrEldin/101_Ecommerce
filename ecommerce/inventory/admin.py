from django.contrib import admin
from ecommerce.inventory import models

# Register your models here.
admin.site.register(models.Brand)
# admin.site.register(models.Category)
admin.site.register(models.Media)
admin.site.register(models.Product)
admin.site.register(models.ProductAttribute)
admin.site.register(models.ProductAttributeValue)
admin.site.register(models.ProductAttributeValues)
admin.site.register(models.ProductType)
admin.site.register(models.ProductTypeAttribute)
admin.site.register(models.Stock)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "is_active"]
    prepopulated_fields = {"slug": ("name",)}


class ProductInventoryAdmin(admin.ModelAdmin):
    list_display = ("product", "store_price", "sku", "is_active", "id")

admin.site.register(models.ProductInventory, ProductInventoryAdmin)
