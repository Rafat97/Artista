# Generated by Django 3.0.4 on 2020-06-17 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artistArt', '0003_auto_20200616_1719'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artistart',
            options={'ordering': ['id']},
        ),
    ]