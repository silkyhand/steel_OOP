# Generated by Django 2.2.19 on 2023-04-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20230403_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productincart',
            old_name='weight',
            new_name='weight_nmb',
        ),
        migrations.AlterField(
            model_name='productincart',
            name='nmb',
            field=models.IntegerField(default=1, verbose_name='Количество'),
        ),
    ]
