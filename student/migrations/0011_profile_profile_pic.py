# Generated by Django 4.0.3 on 2023-02-08 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_remove_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
