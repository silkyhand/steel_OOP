# Generated by Django 2.2.19 on 2023-05-23 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20230513_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='length',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=4, verbose_name='Длина'),
        ),
    ]