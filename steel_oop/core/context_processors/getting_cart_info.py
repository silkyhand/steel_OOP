from orders.models import ProductInCart


def getting_cart_info(request):
    """Подсчет количества товаров в корзине."""
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True)
    products_total_nmb = products_in_cart.count()

    return locals()