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


def products_list(request, slug):
    subcategories_list = Subcategory.objects.all()
    subcategory = get_object_or_404(Subcategory, slug=slug)
    products_list = subcategory.products.all()
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    
    context = {
        'subcategories_list':  subcategories_list,
        'subcategory': subcategory,
        'products_list': products_list,
    }
    if subcategory.category.slug == "listovoy":
        template = 'products/list_products_list.html'
    else:
        template = 'products/list_products_not_list.html'   

    return render(request, template, context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    length = product.length                                
    cart_product_form = CartAddProductForm(length=length)
    return render(request, 'products/product_detail.html', {'product': product,
                                                            'cart_product_form': cart_product_form})