# Generated by Django 3.1.5 on 2021-01-28 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0018_auto_20210128_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]