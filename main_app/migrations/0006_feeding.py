# Generated by Django 4.1.3 on 2022-11-28 10:35

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_delete_uploadimage_finch_finch_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('meal', models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')], default='B', max_length=1)),
            ],
        ),
    ]