# Generated by Django 3.2 on 2022-07-15 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('stat', models.CharField(choices=[('COURAGE', 'Courage'), ('COOL', 'Cool'), ('SUN_PROTECTION', 'Sun Protection'), ('SPELL_CASTING', 'Spell Casting'), ('STEALTH', 'Stealth')], default='COURAGE', max_length=50)),
                ('price', models.IntegerField()),
                ('color', models.CharField(choices=[('PURPLE', 'Purple'), ('NAVY', 'Navy'), ('PINK', 'Pink'), ('GREEN', 'Green'), ('ORANGE', 'Orange')], default='PURPLE', max_length=20)),
                ('variable_one', models.CharField(blank=True, max_length=254, null=True)),
                ('variable_two', models.CharField(blank=True, max_length=254, null=True)),
                ('variable_three', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]