from decimal import Decimal

from django.conf import settings
from products.models import Product


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, unit, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        product_id = str(product.id)
        self.cart.clear()
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'unit': unit,
                                     'price_tonn': str(product.price_tonn),
                                     'price_item': str(product.price_item),
                                     'length': str(product.length),
                                     'coeff': str(product.coeff),                                     
                                     }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        print(self.cart[product_id])    
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product):
        """
        Удаление товара из корзины.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()   

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        products = Product.objects.filter(id__in=product_ids)
        print(list(products.values()))
        for product in products:
            self.cart[str(product.id)]['product'] = product
            self.cart[str(product.id)]['category'] = product.subcategory.category.slug 

        for item in self.cart.values():
            item['price_tonn'] = Decimal(item['price_tonn'])
            item['price_item'] = Decimal(item['price_item'])
            item['length'] = int(item['length'])
            item['coeff'] = Decimal(item['coeff'])
            if item['unit'] == 't':
                item['total_price'] = item['price_tonn'] * item['quantity']
            else:
                # if item['category'] == 'listovoy':            
                #     item['total_price'] = item['price_item'] * item['quantity']
                # elif item['category'] != 'listovoy' and (item['quantaty'] % item['length']) != 0:
                #     raise ValueError('Значение должно быть кратным длине')
                # else:
                #     item['total_price'] = item['price_item'] * item['quantity']
                # while True:
                #     if (item['quantity'] % item['length']) != 0:
                #         raise ValueError('Значение должно быть кратным длине') 
                #     else:   
                item['total_price'] = item['price_item'] * item['quantity']                
            yield item        

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(item['total_price'] for item in self.cart.values())
    
    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True