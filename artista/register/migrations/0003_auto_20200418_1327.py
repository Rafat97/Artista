# Generated by Django 3.0.4 on 2020-04-18 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default='<FUNCTION UUID4 AT 0X000001F5FF67D708>', editable=False),
        ),
    ]
