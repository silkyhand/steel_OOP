from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from orders.forms import CartAddProductForm
from products.models import Product


class ProductListView(ListView):
    model = Product

# def index(request):
#     template = 'products/index.html'
#     return render(request, template)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    length = product.length                                
    cart_product_form = CartAddProductForm(length=length)
    return render(request, 'products/product_detail.html', {'product': product,
                                                            'cart_product_form': cart_product_form})