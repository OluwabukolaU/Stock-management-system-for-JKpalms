# Generated by Django 4.2.5 on 2023-09-20 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0010_alter_stock_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='export_to_CSV',
            field=models.BooleanField(default=True),
        ),
    ]
