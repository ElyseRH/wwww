# Generated by Django 3.2 on 2022-07-20 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220719_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]