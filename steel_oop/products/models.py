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


class Product(models.Model):
    size = models.CharField('Размер', max_length=50)        
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        related_name='products_not_list',
        verbose_name='Категория товара',
    )
    price_tonn = models.IntegerField('Цена за тонну')   
    base_price = models.IntegerField('Базовая цена')
    coeff = models.DecimalField(
        'Коэфф. пересчета',
        max_digits=7,
        decimal_places=3,
        validators=[
            MinValueValidator(1)])
    discount = models.IntegerField('Скидка в процентах', blank=True, default=0)

    def __str__(self):
        return self.subcategory.name

    def save(self, *args, **kwargs):
        self.price_tonn = round(self.base_price/100) * (100 - self.discount)
        super(Product, self).save(*args, **kwargs)


class ProductNotList(Product):    
    parameter = models.CharField('Параметры, марка стали', max_length=50)
    length = models.IntegerField('Длина')    
    price_metr =  models.DecimalField(
        'Цена за п/м',
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(1)])
    
    class Meta:
        ordering = ['-base_price']
        verbose_name = 'Товар не лист'
        verbose_name_plural = ' Товары не листы'
    
    def save(self, *args, **kwargs):
        "Расчитать стоимость погонного метра"
        self.price_metr = self.price_tonn / self.coeff
        super(Product, self).save(*args, **kwargs)


class ProductList(Product):
    thickness = models.CharField('Толщина', max_length=50)   
    area = models.DecimalField(
        'Квадратные метры',
        max_digits=7,
        decimal_places=3,
        validators=[
            MinValueValidator(1)]) 
    price_item = models.IntegerField('Цена за штуку')  
    
    class Meta:
        ordering = ['-base_price']
        verbose_name = 'Лист'
        verbose_name_plural = ' Листы'
  
    def save(self, *args, **kwargs):
        "Расчитать стоимость погонного листа"
        self.price_item = self.price_tonn / self.coeff
        super(Product, self).save(*args, **kwargs)
