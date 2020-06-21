# Generated by Django 3.0.4 on 2020-06-16 11:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('artistArt', '0002_artistart_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistart',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artistart',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]