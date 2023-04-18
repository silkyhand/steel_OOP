from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from products.models import Product
from .forms import OrderCreateForm
from .models import Order, ProductInCart, ProductInOrder


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
    if not session_key:
        request.session.cycle_key()
        session_key = request.session.session_key

    product = get_object_or_404(ProductInCart, session_key=session_key, id=product_id)
    product.delete()

    messages.success(request, 'Item removed from cart.')
    return redirect('orders:cart_order')


def order_create(request):
    session_key = request.session.session_key
    if request.method == 'POST':
        form = OrderCreateForm(request.POST, request=request)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
                print(order.user)             
            order.save()    
            products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True)            
            total_price = 0
            total_weight = 0
            for item in products_in_cart:
                ProductInOrder.objects.create(
                    product=item.product, 
                    nmb=item.nmb,
                    price_item=item.price_item,
                    total_price=item.total_price,
                    weight_nmb=item.weight_nmb,
                    order=order)
                total_price += item.total_price  
                total_weight += item.weight_nmb
                # item.is_active = False
                item.save()
            order.total_price = total_price
            order.total_weight = total_weight
            order.save()     
            messages.success(request, 'Заказ успешно создан.')
            return redirect('orders:order_detail', order_id=order.id)        
    else:
        form = OrderCreateForm(request=request)
        total_price = 0
        total_weight = 0
        products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True)
        for item in products_in_cart:
            total_price += item.total_price  
            total_weight += item.weight_nmb
        context = {
            'form': form,
            'products_in_cart': products_in_cart,  
            'total_price': total_price, 
            'total_weight': total_weight,
        }   

    return render(request, 'orders/order_create.html', context)


def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id) 
    products_in_order = order.products.all()  
    context = { 
        "order": order,
        "products_in_order": products_in_order, 
    }     
    return render(request, 'orders/order_detail.html', context)

         

    # form = CheckoutContactForm(request.POST or None)
    # if request.POST:
    #     print(request.POST)
    #     if form.is_valid():
    #         print("yes")
    #         data = request.POST
    #         name = data.get("name", "3423453")
    #         phone = data["phone"]
    #         user, created = User.objects.get_or_create(username=phone, defaults={"first_name": name})

    #         order = Order.objects.create(user=user, customer_name=name, customer_phone=phone, status_id=1)

    #         for name, value in data.items():
    #             if name.startswith("product_in_basket_"):
    #                 product_in_basket_id = name.split("product_in_basket_")[1]
    #                 product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)
    #                 print(type(value))

    #                 product_in_basket.nmb = value
    #                 product_in_basket.order = order
    #                 product_in_basket.save(force_update=True)

    #                 ProductInOrder.objects.create(product=product_in_basket.product, nmb = product_in_basket.nmb,
    #                                                 price_per_item=product_in_basket.price_per_item,
    #                                                 total_price = product_in_basket.total_price,
    #                                                 order=order)

    #         return HttpResponseRedirect(request.META['HTTP_REFERER'])
    #     else:
    #         print("no")
    # return render(request, 'orders/checkout.html', locals())



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