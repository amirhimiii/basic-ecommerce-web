# Generated by Django 4.0.5 on 2022-06-28 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_order_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
