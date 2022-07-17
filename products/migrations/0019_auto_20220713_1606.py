# Generated by Django 2.2.13 on 2022-07-13 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_product_discount_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('L', 'Large'), ('S', 'Small'), ('M', 'Medium')], max_length=1),
        ),
    ]