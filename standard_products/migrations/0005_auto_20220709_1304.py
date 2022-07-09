# Generated by Django 3.2 on 2022-07-09 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('standard_products', '0004_auto_20220709_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='standardproduct',
            name='stat_one',
        ),
        migrations.RemoveField(
            model_name='standardproduct',
            name='stat_two',
        ),
        migrations.AddField(
            model_name='standardproduct',
            name='stat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='standard_products.stat'),
        ),
    ]
