# Generated by Django 3.0.3 on 2020-03-07 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
