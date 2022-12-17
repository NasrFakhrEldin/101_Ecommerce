from ecommerce.inventory.models import Category


def categories(request):
    return {
        'categories': Category.objects.all()
    }