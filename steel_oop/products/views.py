from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, render

from products.models import Subcategory


def index(request):
    subcategories = Subcategory.objects.all().order_by(Lower('name'))
    context = {
        'subcategories': subcategories,
    }

    return render(request, 'products/index.html', context)


def products_list(request, slug):
    subcategories_list = Subcategory.objects.all()
    subcategory = get_object_or_404(Subcategory, slug=slug)
    products_list = subcategory.products.all()
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    context = {
        'subcategories_list': subcategories_list,
        'subcategory': subcategory,
        'products_list': products_list,
    }
    if subcategory.category.slug == "listovoy":
        template = 'products/list_products_list.html'
    else:
        template = 'products/list_products_not_list.html'

    return render(request, template, context)
