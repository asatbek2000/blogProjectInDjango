# Generated by Django 3.1.5 on 2021-01-29 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0028_auto_20210128_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
    ]
