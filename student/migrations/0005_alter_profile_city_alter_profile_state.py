# Generated by Django 4.0.3 on 2023-02-08 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_remove_profile_location_profile_address_profile_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=250, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(max_length=250, verbose_name='State'),
        ),
    ]
