from django.contrib.sessions.models import Session
from ecommerce.basket.basket import Basket

session_value = Session.objects.get(pk="mw2k7oeuklxt9zfufnudqlagf8q1prq5")


def basket(request):
    return {
        "basket": Basket(request),
        "print": session_value.get_decoded(),  # test value
    }
