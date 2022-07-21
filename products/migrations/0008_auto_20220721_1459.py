# Generated by Django 3.2 on 2022-07-21 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customisation',
            old_name='assoc_product',
            new_name='associated_product',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='Base Price'),
        ),
    ]
