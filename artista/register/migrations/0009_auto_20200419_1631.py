# Generated by Django 3.0.4 on 2020-04-19 10:31

from django.db import migrations, models
import register.models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_auto_20200419_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='avater/default.jpg', null=True, upload_to=register.models.user_directory_path),
        ),
    ]
