# Generated by Django 4.0.3 on 2023-02-11 06:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0008_alter_university_university_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='search_keyword',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
