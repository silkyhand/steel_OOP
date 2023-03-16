from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from orders.forms import CartAddProductForm
from products.models import Product


class ProductListView(ListView):
    model = Product

# def index(request):
#     template = 'products/index.html'
#     return render(request, template)


def product_detail(request, id):
    product = get_object_or_404(Product,
                                id=id,)
                                # slug=slug,
                                # available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'products/product_detail.html', {'product': product,
                                                            'cart_product_form': cart_product_form})