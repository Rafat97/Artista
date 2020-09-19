# Generated by Django 3.0.4 on 2020-09-19 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0023_auto_20200919_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistReviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('post_status', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='public', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_reviewer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_reviewer', to='register.User')),
                ('user_reviewing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_reviewing', to='register.User')),
            ],
        ),
    ]
