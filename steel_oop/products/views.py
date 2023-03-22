from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from orders.forms import CartAddProductForm
from products.models import Product, Subcategory


# class SubcategoryListView(ListView):
#     model = Subcategory

# def index(request):
#     template = 'products/index.html'
#     return render(request, template)

def subcategory_products(request, slug):
    subcategories_list = Subcategory.objects.all()
    subcategory = get_object_or_404(Subcategory, slug=slug)
    products_list = subcategory.products.all()
    context = {
        'subcategories_list':  subcategories_list,
        'subcategory': subcategory,
        'products_list': products_list,
    }

    return render(request, 'posts/group_list.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    length = product.length                                
    cart_product_form = CartAddProductForm(length=length)
    return render(request, 'products/product_detail.html', {'product': product,
                                                            'cart_product_form': cart_product_form})