from adminsortable.models import Sortable
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.shortcuts import reverse

User = get_user_model()


class Category(models.Model):
    name_cat = models.CharField('Группа товаров', max_length=250)
    slug = models.SlugField(max_length=50, unique=True)
    discount = models.IntegerField('Скидка в процентах', blank=True, default=0)

    def get_absolute_url(self):
        return reverse('products:products_category', args=[self.slug])

    def __str__(self):
        return self.name_cat

    class Meta:
        verbose_name = 'Группа товаров'
        verbose_name_plural = 'Группы товаров'


class Subcategory(models.Model):
    name = models.CharField('Категория товаров', max_length=250)
    slug = models.SlugField(max_length=50, unique=True)
    category = models.ForeignKey(
        Category,
        verbose_name='Группа товаров',
        on_delete=models.CASCADE,
        related_name='subcategories'
    )

    def get_absolute_url(self):
        return reverse('products:products_subcategory',
                       kwargs={'cat_slug': self.category.slug,
                               'subcat_slug': self.slug}
                       )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'
        ordering = ('name',)


class Product(Sortable):
    size = models.CharField('Размер', max_length=50)
    parameter = models.CharField(
        'Параметры, марка стали',
        max_length=50,
        null=True,
        blank=True)
    thickness = models.CharField(
        'Толщина',
        max_length=50,
        null=True,
        blank=True)
    length = models.DecimalField(
        'Длина',
        max_digits=4,
        decimal_places=1,
        default=1,
    )
    weight_item = models.DecimalField(
        'Вес ед, кг.',
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    area = models.DecimalField(
        'Квадратные метры',
        max_digits=7,
        decimal_places=3,
        null=True, blank=True)
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Категория товара',
    )
    base_price = models.IntegerField('Базовая цена', default=0)
    coeff = models.DecimalField(
        'Коэфф. пересчета',
        max_digits=7,
        decimal_places=2,
        validators=[
            MinValueValidator(1)])
    price_tonn = models.IntegerField('Цена за тонну', default=0)
    price_item = models.DecimalField(
        'Цена за ед.(п/м или шт.)',
        max_digits=7,
        decimal_places=1,
        default=0)

    def __str__(self):
        return self.subcategory.name

    def get_absolute_url(self):
        return reverse('products:product_detail',
                       kwargs={'product_id': self.pk})

    class Meta(Sortable.Meta):
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def save(self, *args, **kwargs):
        "Расчитать вес, стоимость тонны и погонного метра единицы товара"
        discount = self.subcategory.category.discount
        self.weight_item = (self.length / self.coeff) * 1000
        self.price_tonn = round(
            ((self.base_price / 100) * (100 - discount)) / 100) * 100
        if self.subcategory.category.slug == 'listovoy':
            self.price_item = round(self.price_tonn / self.coeff / 100) * 100
        else:
            self.price_item = round(self.price_tonn / self.coeff, 1)
        super(Product, self).save(*args, **kwargs)


class Productlist(Product):
    class Meta:
        proxy = True
        verbose_name = 'Товар лист'
        verbose_name_plural = 'Товары Листы'


class ProductNotlist(Product):
    class Meta:
        proxy = True
        verbose_name = 'Товар не лист'
        verbose_name_plural = 'Товары не листы'


# class ProductNotList(Product):
#     parameter = models.CharField('Параметры, марка стали', max_length=50)
#     length = models.IntegerField('Длина')
#     price_tonn = models.IntegerField('Цена за тонну', default=0)
#     price_metr = models.DecimalField(
#         'Цена за п/м',
#         max_digits=5,
#         decimal_places=1,
#         validators=[
#             MinValueValidator(0)], default=0)

#     class Meta:
#         ordering = ['-base_price']
#         verbose_name = 'Товар не лист'
#         verbose_name_plural = ' Товары не листы'

#     def save(self, *args, **kwargs):
#         "Расчитать стоимость тонны и погонного метра"
#         self.price_tonn = round(self.base_price/100) * (100 - self.discount)
#         self.price_metr = round(self.price_tonn / self.coeff, 1)
#         super(ProductNotList, self).save(*args, **kwargs)


# class ProductList(Product):
#     thickness = models.CharField('Толщина', max_length=50)
#     area = models.DecimalField(
#         'Квадратные метры',
#         max_digits=7,
#         decimal_places=3,
#         validators=[
#             MinValueValidator(1)])
#     price_tonn = models.IntegerField('Цена за тонну', default=0)
#     price_item = models.IntegerField('Цена за штуку', default=0)

#     class Meta:
#         ordering = ['-base_price']
#         verbose_name = 'Лист'
#         verbose_name_plural = ' Листы'

#     def save(self, *args, **kwargs):
#         "Расчитать стоимость тонны и листа"
#         self.price_tonn = round(self.base_price/100) * (100 - self.discount)
#         self.price_item = round(self.price_tonn / self.coeff / 100) * 100
#         super(ProductList, self).save(*args, **kwargs)
