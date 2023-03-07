from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.shortcuts import reverse


User = get_user_model()


class Category(models.Model):
    name_cat = models.CharField('Группа товаров', max_length=250)
    slug = models.SlugField(max_length=50, unique=True)

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


class ProductNotList(models.Model):
    size = models.CharField('Размер', max_length=50)
    parameter = models.CharField('Параметры, марка стали', max_length=50)
    length = models.IntegerField('Длина')
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        related_name='products_not_list',
        verbose_name='Категория товара',
    )
    base_price = models.IntegerField('Базовая цена')
    coeff = models.DecimalField(
        'Коэфф. пересчета',
        max_digits=7,
        decimal_places=2,
        validators=[
            MinValueValidator(1)])
    discount = models.IntegerField('Скидка в процентах', blank=True, default=0)

    @property
    def price_tonn(self):
        '''Расчитать стоимость со скидкой'''
        return int(self.base_price * (100 - self.discount) / 100)

    @property
    def price_metr(self):
        "Расчитать стоимость тонны"
        price_metr = self.price_tonn / self.coeff
        return round(price_metr, 1)

    def __str__(self):
        return self.subcategory.name

    class Meta:
        ordering = ['-base_price']
        verbose_name = 'Товар не лист'
        verbose_name_plural = ' Товары не листы'


class ProductList(models.Model):
    thickness = models.CharField('Толщина', max_length=50)
    size = models.CharField('Размер', max_length=50)
    area = models.DecimalField(
        'Квадратные метры',
        max_digits=7,
        decimal_places=3,
        validators=[
            MinValueValidator(1)])
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        related_name='products_list',
        verbose_name='Категория товара',
    )
    base_price = models.IntegerField('Базовая цена')
    coeff = models.DecimalField(
        'Коэфф. пересчета',
        max_digits=7,
        decimal_places=2,
        validators=[
            MinValueValidator(1)])
    discount = models.IntegerField('Скидка в процентах', blank=True, default=0)

    @property
    def price_tonn(self):
        '''Расчитать стоимость со скидкой'''
        return int(self.base_price * (100 - self.discount) / 100)

    @property
    def price_item(self):
        "Расчитать стоимость тонны"
        price_metr = self.price_tonn / self.coeff
        return round(price_metr, 1)

    def __str__(self):
        return self.subcategory.name

    class Meta:
        ordering = ['-base_price']
        verbose_name = 'Лист'
        verbose_name_plural = ' Листы'
