from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from .models import ProductInCart


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    length = product.length
    form = CartAddProductForm(request.POST, length=length)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'],                 
                 unit=cd['unit'],
                )
    return redirect('orders:cart_detail')
    # else:
    #     print(form.errors)
    # return render(request, 'orders:cart_add', {'product_id': product_id})


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('orders:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


def cart_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("nmb")
   
    new_product = ProductInCart.objects.create(
        session_key=session_key,
        product_id=product_id,
        nmb=nmb,
    )
    products_total_nmb = ProductInCart.objects.filter(session_key=session_key, is_active=True).count()
    return_dict["products_total_nmb"] = products_total_nmb

    
    return JsonResponse(return_dict)
