from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from ecommerce.ecommerce_auth.managers import EcommerceUserManager
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):

    email = models.EmailField(_("email address"), unique=True)

    # Delivery details
    about = models.TextField(_("about"), max_length=500, blank=True)
    country = CountryField()
    phone_number = PhoneNumberField(_("Phone Number"), blank=True)
    postcode = models.CharField(_("postcode"), max_length=12, blank=True)
    address_line_1 = models.CharField(_("address_line_1"), max_length=150, blank=True)
    address_line_2 = models.CharField(_("address_line_2"), max_length=150, blank=True)
    town_city = models.CharField(_("town_city"), max_length=150, blank=True)

    objects = EcommerceUserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.email


"""
NOTES:
    - AbstractUser: Use this option if you are happy with the existing fields on the User model
        and just want to remove the username field.

    - AbstractBaseUser: Use this option if you want to start from scratch by creating your own,
        completely new User model.

    - USERNAME_FIELD: A string describing the name of the field on the user model
        that is used as the unique identifier. by default username

    - REQUIRED_FIELDS: A list of the field names that will be prompted for
        when creating a user via the createsuperuser management command. by default email

    - REF:
        https://testdriven.io/blog/django-custom-user-model/
        https://medium.com/agatha-codes/options-objects-customizing-the-django-user-model-6d42b3e971a4
        https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
        https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#writing-a-manager-for-a-custom-user-model
        https://stackoverflow.com/a/72320454/20343397
        https://docs.djangoproject.com/en/3.2/topics/auth/customizing/

"""
