# Generated by Django 3.0.4 on 2020-04-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20200418_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='avater/default.jpg', null=True, upload_to='avater/%Y-%M-%D'),
        ),
    ]
