# Generated by Django 4.1.3 on 2022-11-27 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_uploadimage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadImage',
        ),
        migrations.AddField(
            model_name='finch',
            name='finch_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]