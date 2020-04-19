# Generated by Django 3.0.4 on 2020-04-19 11:23

from django.db import migrations, models
import register.models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_auto_20200419_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar/default.jpg', height_field=200, null=True, upload_to=register.models.user_directory_path, width_field=200),
        ),
    ]
