# Generated by Django 3.1.5 on 2021-02-01 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0048_remove_blogcomment_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcomment',
            options={'ordering': ('created_on',)},
        ),
        migrations.RenameField(
            model_name='blogcomment',
            old_name='publish',
            new_name='created_on',
        ),
    ]
