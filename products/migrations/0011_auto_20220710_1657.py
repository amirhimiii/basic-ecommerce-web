# Generated by Django 2.2.13 on 2022-07-10 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20220709_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingaddress',
            name='f_name',
            field=models.CharField(default='a', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='l_name',
            field=models.CharField(default='a', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='number',
            field=models.IntegerField(blank=True, default=91200000),
            preserve_default=False,
        ),
    ]
