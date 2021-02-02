# Generated by Django 3.1.5 on 2021-01-28 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0021_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish'), (2, 'Delete')], default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish'), (2, 'Delete')], default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish'), (2, 'Delete')], default=0),
        ),
    ]