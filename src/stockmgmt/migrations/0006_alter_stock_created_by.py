# Generated by Django 4.2.5 on 2023-09-20 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0005_alter_stock_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='created_by',
            field=models.CharField(blank=True, default='Anonymous', max_length=50),
        ),
    ]
