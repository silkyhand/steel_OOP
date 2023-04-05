from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from .models import ProductInCart


# @require_POST
# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     length = product.length
#     form = CartAddProductForm(request.POST, length=length)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product,
#                  quantity=cd['quantity'],
#                  update_quantity=cd['update'],                 
#                  unit=cd['unit'],
#                 )
#     return redirect('orders:cart_detail')
    # else:
    #     print(form.errors)
    # return render(request, 'orders:cart_add', {'product_id': product_id})


# def cart_remove(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     cart.remove(product)
#     return redirect('orders:cart_detail')


# def cart_detail(request):
#     cart = Cart(request)
#     return render(request, 'cart/cart_detail.html', {'cart': cart})


def cart_adding(request):
    return_dict = dict()
    session_key = request.session.session_key   
    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("nmb")    
   
    new_product, created = ProductInCart.objects.get_or_create(
        session_key=session_key,
        product_id=product_id,
        defaults={"nmb": nmb}        
    )

    if not created:        
        new_product.nmb += int(nmb)
        new_product.save(force_update=True)
         
    products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True)
    products_total_nmb = products_in_cart.count()
    return_dict["products_total_nmb"] = products_total_nmb

    return_dict["products"] = list()

    for item in products_in_cart:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.subcategory.name
        product_dict["price_item"] = item.price_item
        product_dict["nmb"] = item.nmb
        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)


def cart_order(request):
    session_key = request.session.session_key
    products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True)
    total_cart_price = 0
    for item in products_in_cart:
        total_cart_price += item.total_price        
    template = "cart/cart_order.html"
    context = {
        "total_cart_price": total_cart_price,
        "products_in_cart": products_in_cart,               
    }   
    return render(request, template, context)


def cart_update(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
        session_key = request.session.session_key

    products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True)
    # if not cart:
    #     cart = Cart.objects.create(session_key=session_key)

    for product in products_in_cart.all():
        product.nmb = request.POST.get(f'nmb_{product.id}')
        product.save()

    messages.success(request, 'Cart updated.')
    return redirect('orders:cart_order')


def cart_remove(request, product_id):
    session_key = request.session.session_key
    # if not session_key:
    #     request.session.cycle_key()
    #     session_key = request.session.session_key

    product = get_object_or_404(ProductInCart, session_key=session_key, id=product_id)
    product.delete()

    messages.success(request, 'Item removed from cart.')
    return redirect('orders:cart_order')

