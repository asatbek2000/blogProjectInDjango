# Generated by Django 3.1.5 on 2021-01-28 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0027_subscribe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]
