# Generated by Django 3.1.5 on 2021-01-27 12:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_auto_20210127_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blogapp.post'),
            preserve_default=False,
        ),
    ]
