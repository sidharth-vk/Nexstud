# Generated by Django 4.0.3 on 2023-02-08 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_remove_profile_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
    ]
