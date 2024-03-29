# Generated by Django 2.2.19 on 2023-04-17 20:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_product_weight_item'),
        ('orders', '0005_auto_20230413_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Комментарии')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Общая стоимость товаров в заказе')),
                ('total_weight', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Общий вес товаров в заказе')),
                ('status', models.CharField(choices=[('new', 'Новый'), ('in_progress', 'В обработке'), ('done', 'Выполнен')], default='new', max_length=20, verbose_name='Статус заказа')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmb', models.PositiveIntegerField(default=1)),
                ('weight_nmb', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Общий вес товара в корзине')),
                ('price_item', models.DecimalField(decimal_places=1, default=0, max_digits=7, verbose_name='Цена за ед.(п/м или шт.)')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Общая стоимость товара в корзине')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='orders.Order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='products.Product', verbose_name='Товар в заказе')),
            ],
            options={
                'verbose_name': 'Товар в заказе',
                'verbose_name_plural': 'Товары в заказе',
            },
        ),
    ]
