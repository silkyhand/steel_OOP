# Generated by Django 2.2.19 on 2023-03-13 18:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cat', models.CharField(max_length=250, verbose_name='Группа товаров')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Группа товаров',
                'verbose_name_plural': 'Группы товаров',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Категория товаров')),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='products.Category', verbose_name='Группа товаров')),
            ],
            options={
                'verbose_name': 'Категория товаров',
                'verbose_name_plural': 'Категории товаров',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=50, verbose_name='Размер')),
                ('parameter', models.CharField(blank=True, max_length=50, null=True, verbose_name='Параметры, марка стали')),
                ('thickness', models.CharField(blank=True, max_length=50, null=True, verbose_name='Толщина')),
                ('length', models.IntegerField(blank=True, null=True, verbose_name='Длина')),
                ('area', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True, verbose_name='Квадратные метры')),
                ('base_price', models.IntegerField(default=0, verbose_name='Базовая цена')),
                ('coeff', models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Коэфф. пересчета')),
                ('price_tonn', models.IntegerField(default=0, verbose_name='Цена за тонну')),
                ('price_item', models.DecimalField(decimal_places=1, default=0, max_digits=5, verbose_name='Цена за ед.(п/м или шт.)')),
                ('discount', models.IntegerField(blank=True, default=0, verbose_name='Скидка в процентах')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_not_list', to='products.Subcategory', verbose_name='Категория товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-base_price'],
            },
        ),
        migrations.CreateModel(
            name='Productlist',
            fields=[
            ],
            options={
                'verbose_name': 'Товар лист',
                'verbose_name_plural': 'Товары Листы',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('products.product',),
        ),
        migrations.CreateModel(
            name='ProductNotlist',
            fields=[
            ],
            options={
                'verbose_name': 'Товар не лист',
                'verbose_name_plural': 'Товары не листы',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('products.product',),
        ),
    ]
