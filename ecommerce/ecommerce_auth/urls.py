from django.contrib import admin
from django.urls import include, path
from django_registration.backends.activation.views import RegistrationView
from ecommerce.ecommerce_auth import views
from ecommerce.ecommerce_auth.forms import EcommerceRegistrationForm

# app_name = "ecommerce_auth"

urlpatterns = [
    path(
        "register/",
        RegistrationView.as_view(form_class=EcommerceRegistrationForm),
        name="django_registration_register",
    ),
    path(
        "",
        include("django_registration.backends.activation.urls"),
    ),
    path(
        "profile/",
        views.profile,
        name="profile",
    ),
]
