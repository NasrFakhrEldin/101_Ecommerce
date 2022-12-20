"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

import dj_database_url
from configurations import Configuration, values


class Dev(Configuration):

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = values.SecretValue()

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = ["127.0.0.1"]

    # Application definition

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django_registration",
        "crispy_forms",
        "crispy_bootstrap5",
        # Local Apps
        "ecommerce.dashboard",
        "ecommerce.inventory",
        "ecommerce.demo",
        "ecommerce.drf",
        "ecommerce.search",
        "ecommerce.dninja",
        "ecommerce.promotion",
        "ecommerce.cbv",
        "ecommerce.basket",
        "ecommerce.ecommerce_auth",
        # External Apps
        "mptt",
        "django_elasticsearch_dsl",
        "rest_framework",
        "ninja",
        "django_celery_beat",
        "phonenumber_field",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "ecommerce.urls"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [BASE_DIR / "templates"],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                    "ecommerce.basket.context_processors.basket",
                    "ecommerce.cbv.context_processors.categories",
                ],
            },
        },
    ]

    WSGI_APPLICATION = "ecommerce.wsgi.application"

    # Database
    # https://docs.djangoproject.com/en/4.1/ref/settings/#databases

    # DATABASES = {
    #     "default": {
    #         "ENGINE": "django.db.backends.sqlite3",
    #         "NAME": BASE_DIR / "db.sqlite3",
    #     }
    # }

    # DATABASES = {
    #     "default": {
    #         "ENGINE": "django.db.backends.postgresql_psycopg2",
    #         "NAME": "db_101_ecommerce",
    #         "USER": "101ecommerceuser",
    #         "PASSWORD": "mypass",
    #         "HOST": "127.0.0.1",
    #         "PORT": "5432",
    #     }
    # }

    DATABASES = {
        "default": dj_database_url.config(
            default=f"postgres://101ecommerceuser:mypass@pgdb:5432/db_101_ecommerce"
        ),
    }

    # Password validation
    # https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/4.1/topics/i18n/

    LANGUAGE_CODE = "en-us"

    TIME_ZONE = "UTC"

    USE_I18N = True

    USE_L10N = True

    # USE_TZ = False

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.1/howto/static-files/

    STATIC_URL = "/static/"
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

    # Default primary key field type
    # https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    ELASTICSEARCH_DSL = {"default": {"hosts": "localhost:9200"}}

    REST_FRAMEWORK = {
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
        "PAGE_SIZE": 25,
    }
    from celery.schedules import crontab

    CELERY_BROKER_URL = "redis://redis:6379"
    CELERY_RESULT_BACKEND = "redis://redis:6379"
    CELERY_BEAT_SCHEDULE = {
        "sample_task": {
            "task": "ecommerce.promotion.tasks.promotion_managment_is_active",
            "schedule": crontab(minute="0", hour="1"),
        },
    }

    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    # AUTH_APP
    AUTH_USER_MODEL = "ecommerce_auth.User"
    # Two-Step Activation
    ACCOUNT_ACTIVATION_DAYS = 3

    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

    CRISPY_TEMPLATE_PACK = "bootstrap5"
