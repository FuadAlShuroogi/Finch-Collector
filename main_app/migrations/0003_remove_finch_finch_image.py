# Generated by Django 4.1.3 on 2022-11-27 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_finch_finch_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finch',
            name='finch_image',
        ),
    ]
