# Generated by Django 4.0.3 on 2023-02-08 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_rename_lead_newleads'),
    ]

    operations = [
        migrations.CreateModel(
            name='newlead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leadname', models.CharField(blank=True, max_length=250, null=True, verbose_name='Lead Name')),
                ('PhoneNo', models.PositiveIntegerField(blank=True, null=True, verbose_name='Phone No')),
            ],
        ),
        migrations.DeleteModel(
            name='newleads',
        ),
    ]
