# Generated by Django 4.0.3 on 2023-02-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phoneno',
        ),
        migrations.AddField(
            model_name='profile',
            name='userid',
            field=models.CharField(default=2, max_length=50, unique=True, verbose_name='User ID'),
            preserve_default=False,
        ),
    ]