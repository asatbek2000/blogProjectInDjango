# Generated by Django 3.1.5 on 2021-01-27 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0013_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='phone',
        ),
    ]
