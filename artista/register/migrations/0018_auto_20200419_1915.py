# Generated by Django 3.0.4 on 2020-04-19 13:15

from django.db import migrations, models
import register.models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0017_auto_20200419_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar/default.jpg', upload_to=register.models.user_directory_path),
        ),
    ]
