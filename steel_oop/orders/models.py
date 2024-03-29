from django.contrib.auth import get_user_model
from django.db import models
from products.models import Product

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        null=True,
        blank=True)
    name = models.CharField('Имя', max_length=255)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Почта')
    comments = models.TextField('Комментарии', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(
        'Общая стоимость товаров в заказе',
        max_digits=10, decimal_places=2, default=0,
    )
    total_weight = models.DecimalField(
        'Общий вес товаров в заказе',
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    STATUS_CHOICES = (
        ('new', 'Новый'),
        ('in_progress', 'В обработке'),
        ('done', 'Выполнен'),
    )
    status = models.CharField('Статус заказа',
                              max_length=20,
                              choices=STATUS_CHOICES,
                              default='new')

    def __str__(self):
        return f'Заказ №{self.id}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        if self.user:
            discount_price = round(
                ((self.total_price * (100 - self.user.user_discount)) / 100), 1)
            self.total_price = discount_price
            print(self.total_price)
        else:
            self.total_price = self.total_price
        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(
        Order,
        verbose_name='Заказ',
        on_delete=models.CASCADE,
        related_name='products')
    product = models.ForeignKey(Product,
                                verbose_name='Товар в заказе',
                                on_delete=models.CASCADE,
                                related_name="order_products")
    nmb = models.PositiveIntegerField(default=1)
    weight_nmb = models.DecimalField(
        'Общий вес товара в корзине',
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

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def get_cost(self):
        return self.price * self.quantity


class ProductInCart(models.Model):
    session_key = models.CharField(max_length=128)
    product = models.ForeignKey(
        Product,
        verbose_name='Товар в машине',
        on_delete=models.CASCADE,
        related_name='productsincart')
    nmb = models.DecimalField(
        'Количество',
        max_digits=9,
        decimal_places=1,
        default=1,
    )
    weight_nmb = models.DecimalField(
        'Общий вес товаров в машине',
        max_digits=10,
        decimal_places=2,
    )
    price_item = models.DecimalField(
        'Цена за ед.(п/м или шт.)',
        max_digits=7,
        decimal_places=1,
        default=0)
    total_price = models.DecimalField(
        'Общая стоимость товара в машине',
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
        verbose_name = 'Товар в машине'
        verbose_name_plural = 'Товары в машине'

    def save(self, *args, **kwargs):
        price_item = self.product.price_item
        weight_item = float(self.product.weight_item)
        length = float(self.product.length)

        self.price_item = price_item
        self.total_price = float(self.nmb) * float(price_item)
        self.weight_nmb = round(float(self.nmb) / length * weight_item)
        super(ProductInCart, self).save(*args, **kwargs)
