# Generated by Django 2.2.13 on 2022-07-10 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_remove_billingaddress_save_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingaddress',
            name='descript',
            field=models.CharField(default='ss', max_length=200),
            preserve_default=False,
        ),
    ]
