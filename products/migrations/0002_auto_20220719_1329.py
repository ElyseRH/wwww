# Generated by Django 3.2 on 2022-07-19 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('Purple', 'Purple'), ('Navy', 'Navy'), ('Pink', 'Pink'), ('Green', 'Green'), ('Orange', 'Orange')], default='PURPLE', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='stat',
            field=models.CharField(choices=[('Courage', 'Courage'), ('Cool', 'Cool'), ('Sun_Protection', 'Sun Protection'), ('Spell_Casting', 'Spell Casting'), ('Stealth', 'Stealth')], default='COURAGE', max_length=50),
        ),
    ]
