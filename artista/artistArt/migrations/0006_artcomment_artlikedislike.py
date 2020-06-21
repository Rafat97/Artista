# Generated by Django 3.0.4 on 2020-06-20 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0019_user_refresh_token'),
        ('artistArt', '0005_auto_20200620_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtLikeDislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_dislike', models.BooleanField(default=False)),
                ('artist_art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artistArt.ArtistArt')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.User')),
            ],
        ),
        migrations.CreateModel(
            name='ArtComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_message', models.CharField(max_length=255)),
                ('artist_art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artistArt.ArtistArt')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.User')),
            ],
        ),
    ]