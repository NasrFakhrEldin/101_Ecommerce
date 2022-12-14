"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# from django_registration.backends.activation.views import RegistrationView

# from ecommerce.ecommerce_auth import views
# from ecommerce.ecommerce_auth.forms import EcommerceRegistrationForm

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("ecommerce.ecommerce_auth.urls")),
    # Registration
    # path(
    #     "accounts/register/",
    #     RegistrationView.as_view(form_class=EcommerceRegistrationForm),
    #     name="django_registration_register",
    # ),
    # path("accounts/", include("django_registration.backends.activation.urls")),
    # path("accounts/profile/", views.profile, name="profile"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("demo/", include("ecommerce.demo.urls", namespace="demo")),
    path("api/v1/", include("ecommerce.drf.urls", namespace="drf")),
    path("dninja/", include("ecommerce.dninja.urls", namespace="dninja")),
    path("", include("ecommerce.cbv.urls", namespace="cbv")),
    path("basket/", include("ecommerce.basket.urls", namespace="basket")),
]
