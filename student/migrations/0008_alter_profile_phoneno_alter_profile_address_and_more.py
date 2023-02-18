# Generated by Django 4.0.3 on 2023-02-08 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_alter_profile_phoneno_alter_profile_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='PhoneNo',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Phone No'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='firstname',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastname',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pincode',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Pincode'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='userid',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='User ID'),
        ),
    ]