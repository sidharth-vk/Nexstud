# Generated by Django 4.0.3 on 2023-02-07 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='university_img',
            field=models.ImageField(default=2, upload_to='university_Image', verbose_name='Image'),
            preserve_default=False,
        ),
    ]
