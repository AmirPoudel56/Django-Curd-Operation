# Generated by Django 5.1 on 2024-08-19 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_registration_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='photo',
            field=models.ImageField(upload_to='profile_picture/'),
        ),
    ]
