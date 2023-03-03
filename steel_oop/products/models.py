# from django.db import models
# from django.contrib.auth import get_user_model
# from django.shortcuts import reverse


# User = get_user_model()


# class Category(models.Model):
#     name_cat = models.CharField('Группа товаров', max_length=250)
#     slug = models.SlugField(max_length=50, unique=True)

#     def get_absolute_url(self):
#         return reverse('products:products_category',  args=[self.slug])
    
#     def __str__(self):
#         return self.name_cat
    
#     class Meta:
#         verbose_name = 'Группа товаров'
#         verbose_name_plural = 'Группы товаров'


# class Subcategory(models.Model):
#     name = models.CharField('Категория товаров', max_length=250)
#     slug = models.SlugField(max_length=50, unique=True)
#     category = models.ForeignKey(
#         Category, 
#         verbose_name='Группа товаров', 
#         on_delete=models.CASCADE,
#         related_name='subcategories'
#         )

#     def get_absolute_url(self):
#         return reverse('products:products_subcategory',
#                        kwargs={'cat_slug': self.category.slug,
#                                'subcat_slug': self.slug}
#                        )

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         verbose_name = 'Категория товаров'
#         verbose_name_plural = 'Категории товаров'


# class Specification(models.Model):
#     name = models.CharField('Характеристика', max_length=250)
#     subcategory = models.ForeignKey(
#         Subcategory, 
#         verbose_name='Категория товаров', 
#         on_delete=models.CASCADE,
#         related_name='specifications'
#         )
    
#     class Meta:
#         verbose_name = 'Характеристика товара'
#         verbose_name_plural = 'Характеристики товаров'

#     def __str__(self):
#         return self.name    


# class Product(models.Model):
#     subcategory = models.ForeignKey(
#         Subcategory,
#         on_delete=models.CASCADE,
#         related_name='products',
#         verbose_name='Категория товара',
#         )
#     base_price = models.IntegerField('Базовая цена')
#     coeff_tonne_metre = models.IntegerField('Коэфф. пересчета тонны в метры')
#     discount = models.IntegerField('Скидка в процентах', blank=True, default=0)
    
#     specifications = models.ManyToManyField(
#         'Specification',        
#         through='ProductSpecificationValue',
#         related_name='products',
#         verbose_name='характеристики'
#     )

#     @property
#     def get_discount(self):
#         '''Расчитать стоимость со скидкой'''
#         price = int(self.price * (100 - self.discount) / 100)
#         return price

#     def __str__(self):
#         return self.subcategory.name

#     class Meta:
#         ordering = ['-base_price']
#         verbose_name = 'Товар'
#         verbose_name_plural = 'Товары'


# class ProductSpecificationValue(models.Model):
#     product = models.ForeignKey(
#         Product,
#         on_delete=models.CASCADE,
#         related_name='value'
#         )
#     specification = models.ForeignKey(
#         Specification,
#         on_delete=models.CASCADE,
#         related_name='value'
#         )
#     value = models.CharField('Значение', max_length=50)

#     def __str__(self):
#         return self.value
    
#     class Meta:
#         verbose_name = 'Значение характеристики'
#         verbose_name_plural = 'Значение характеристик'

            
