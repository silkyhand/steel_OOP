from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from orders.forms import CartAddProductForm
from products.models import Category, Product, Subcategory


def index(request):
    category = Category.objects.prefetch_related('subcategories').all()
    context = {
        'category': category,       
    }   
  
    return render(request, 'products/index.html', context)


def subcategory_products(request, slug):
    subcategories_list = Subcategory.objects.all()
    subcategory = get_object_or_404(Subcategory, slug=slug)
    products_list = subcategory.products.all()
    context = {
        'subcategories_list':  subcategories_list,
        'subcategory': subcategory,
        'products_list': products_list,
    }

    return render(request, 'products/subcategory_products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    length = product.length                                
    cart_product_form = CartAddProductForm(length=length)
    return render(request, 'products/product_detail.html', {'product': product,
                                                            'cart_product_form': cart_product_form})