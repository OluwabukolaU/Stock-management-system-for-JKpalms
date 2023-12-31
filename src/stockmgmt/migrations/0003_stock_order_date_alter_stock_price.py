# Generated by Django 4.2.5 on 2023-09-19 22:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0002_stock_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='order_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
