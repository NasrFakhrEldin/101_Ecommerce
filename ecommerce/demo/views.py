from django.shortcuts import render
from ecommerce.inventory import models


def home(request):

    return render(request, "index.html")


def categoty(request):
    all_data = models.Category.objects.all()

    print(all_data.query)

    return render(request, "categories.html", {"all_data": all_data})


def product_by_category(request, category):

    print(category)
    all_data = models.Product.objects.filter(category__name=category).values(
        "id", "name", "slug", "category__name", "product__store_price"
    )

    # all_data = models.ProductInventory.objects.filter(product__category__name=category)
    print(all_data.query)

    return render(request, "product_by_category.html", {"all_data": all_data})


def product_detail(request, slug):
    from django.contrib.postgres.aggregates import ArrayAgg
    from django.db.models import Count
    filter_arguments = []

    if request.GET:
        for value in request.GET.values():
            filter_arguments.append(value)
        # print(filter_arguments)

        # all_data = models.Product.objects.filter(slug=slug)
        # all_data = models.ProductInventory.objects.filter(product__slug=slug).values(
        #     "id", "sku", "product__name", "store_price", "product_inventory__units"
        # )

        # all_data = (
        #     models.ProductInventory.objects.filter(product__slug=slug)
        #     .filter(attribute_values__attribute_value="red")
        #     .filter(attribute_values__attribute_value=5)
        #     .select_related("product")
        # ).values(
        #     "id", "sku", "product__name", "store_price", "product_inventory__units"
        # )

        # all_data = (
        #     models.ProductInventory.objects.filter(product__slug=slug).filter(
        #         attribute_values__attribute_value__in=filter_arguments
        #     )
        # ).values("id", "sku", "product__name", "store_price", "product_inventory__units")

        # all_data = (
        #     models.ProductInventory.objects.filter(product__slug=slug)
        #     .filter(attribute_values__attribute_value=filter_arguments[0])
        #     .filter(attribute_values__attribute_value=filter_arguments[1])
        # ).values("id", "sku", "product__name", "store_price", "product_inventory__units")

        # all_data = (
        #     models.ProductInventory.objects.filter(product__slug=slug)
        #     .filter(attribute_values__attribute_value__in=filter_arguments)
        #     .annotate(num_tags=Count("attribute_values"))
        #     .filter(num_tags=len(filter_arguments))
        # ).values(
        #     "id", "sku", "product__name", "store_price", "product_inventory__units"
        # )
        all_data = (
            models.ProductInventory.objects.filter(product__slug=slug)
            .filter(attribute_values__attribute_value__in=filter_arguments)
            .annotate(num_tags=Count("attribute_values"))
            .filter(num_tags=len(filter_arguments))
        ).values(
            "id", "sku", "product__name", "store_price", "product_inventory__units"
        ).annotate(field=ArrayAgg("attribute_values__attribute_value")).get()
        print(all_data)

    else:

        # all_data = (
        #     models.ProductInventory.objects.filter(product__slug=slug).values(
        #         "id", "sku", "product__name", "store_price", "product_inventory__units"
        #     ).annotate(filed = ArrayAgg("attribute_values__attribute_value")
        #     )
        # )

        all_data = (
            models.ProductInventory.objects.filter(product__slug=slug)
            .filter(is_default=True)
            .values(
                "id", "sku", "product__name", "store_price", "product_inventory__units"
            )
            .annotate(field=ArrayAgg("attribute_values__attribute_value")).get()
        )

        print(all_data)

    dump_one = (
        models.ProductInventory.objects.filter(product__slug=slug)
        .distinct()
        .values(
            "attribute_values__product_attribute__name",
            "attribute_values__attribute_value",
        )
    )
    # print(dump_one)

    dump_two = (
        models.ProductTypeAttribute.objects.filter(
            product_type__product_type__product__slug=slug
        )
        .values("product_attribute__name")
        .distinct()
    )
    # print(dump_two)

    return render(
        request,
        "product_detail.html",
        {"all_data": all_data, "dump_one": dump_one, "dump_two": dump_two},
    )


# https://docs.djangoproject.com/en/4.1/ref/models/expressions/
# Reporter.objects.update(stories_filed=F('stories_filed') + 1)
