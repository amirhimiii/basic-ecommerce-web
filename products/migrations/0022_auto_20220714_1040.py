# Generated by Django 2.2.13 on 2022-07-14 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_comment_new_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='product_comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='new_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.Product'),
        ),
    ]
