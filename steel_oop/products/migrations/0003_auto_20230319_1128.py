# Generated by Django 2.2.19 on 2023-03-19 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230313_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='length',
            field=models.IntegerField(default=1, verbose_name='Длина'),
        ),
    ]
