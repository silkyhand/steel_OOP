# Generated by Django 2.2.19 on 2023-04-03 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_productincart_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productincart',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Вес'),
        ),
    ]