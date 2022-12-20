from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from ecommerce.ecommerce_auth.models import User


class EcommerceUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "about",
                    "country",
                    "phone_number",
                    "postcode",
                    "address_line_1",
                    "address_line_2",
                    "town_city",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )

    list_display = ("email", "username", "first_name", "last_name", "is_staff")
    search_fields = ("email", "username", "first_name", "last_name")
    ordering = ("email",)


admin.site.register(User, EcommerceUserAdmin)
# admin.site.register(User)
