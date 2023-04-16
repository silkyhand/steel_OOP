from decimal import Decimal
from django.contrib.auth import get_user_model
from django.db import models
from products.models import Product

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    customer_name = models.CharField('Имя', max_length=255)
    customer_phone = models.CharField('Телефон', max_length=20)
    customer_email = models.EmailField('Почта')    
    comments = models.TextField('Комментарии', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ('new', 'Новый'),
        ('in_progress', 'В обработке'),
        ('done', 'Выполнен'),
    )
    status = models.CharField('Статус заказа', max_length=20, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return f'Заказ #{self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    

class ProductInOrder(models.Model):
    order = models.ForeignKey(
        Order,
        verbose_name='Товар в заказе',
        on_delete=models.CASCADE,
         related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity    
    


class ProductInCart(models.Model):
    session_key = models.CharField(max_length=128)
    product = models.ForeignKey(
        Product,
        verbose_name='Товар в корзине',
        on_delete=models.CASCADE,
        related_name='productsincart')
    nmb = models.IntegerField('Количество', default=1)
    weight_nmb = models.DecimalField(
        'Общий вес товаров в корзине',
        max_digits=10,
        decimal_places=2,        
    )
    price_item = models.DecimalField(
        'Цена за ед.(п/м или шт.)',
        max_digits=7,
        decimal_places=1,
        default=0)
    total_price = models.DecimalField(
        'Общая стоимость товара в корзине', 
        max_digits=10, decimal_places=2, default=0,
    )
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        if self.product.thickness:
            return f'{self.product.subcategory.name}\n {self.product.thickness}'
               
        return f'{self.product.subcategory.name}\n {self.product.size}'

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def save(self, *args, **kwargs):
        price_item = self.product.price_item
        weight_item = self.product.weight_item
        length = Decimal(self.product.length)

        self.price_item = price_item
        self.total_price = int(self.nmb) * price_item
        self.weight_nmb = round(int(self.nmb) / length * weight_item)        
        super(ProductInCart, self).save(*args, **kwargs)


# class Status(models.Model):
#     name = models.CharField(max_length=24, blank=True, null=True, default=None)
#     is_active = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)

#     def __str__(self):
#         return "Статус %s" % self.name

#     class Meta:
#         verbose_name = 'Статус заказа'
#         verbose_name_plural = 'Статусы заказа'


# class Order(models.Model):
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#total price for all products in order
#     customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
#     customer_email = models.EmailField(blank=True, null=True, default=None)
#     customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
#     customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
#     comments = models.TextField(blank=True, null=True, default=None)
#     status = models.ForeignKey(Status)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)

#     def __str__(self):
#         return "Заказ %s %s" % (self.id, self.status.name)

#     class Meta:
#         verbose_name = 'Заказ'
#         verbose_name_plural = 'Заказы'


# class ProductInOrder(models.Model):
#     order = models.ForeignKey(Order, blank=True, null=True, default=None)
#     product = models.ForeignKey(Product, blank=True, null=True, default=None)
#     nmb = models.IntegerField(default=1)
#     price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#price*nmb
#     is_active = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)

#     def __str__(self):
#         return "%s" % self.product.name

#     class Meta:
#         verbose_name = 'Товар в заказе'
#         verbose_name_plural = 'Товары в заказе'   



