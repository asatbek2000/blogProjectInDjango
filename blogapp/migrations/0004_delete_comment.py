# Generated by Django 3.1.5 on 2021-01-27 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20210127_0631'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
