# Generated by Django 4.0.3 on 2023-02-08 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_alter_profile_phoneno_alter_profile_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='userid',
        ),
    ]
