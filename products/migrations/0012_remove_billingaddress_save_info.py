# Generated by Django 2.2.13 on 2022-07-10 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20220710_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingaddress',
            name='save_info',
        ),
    ]