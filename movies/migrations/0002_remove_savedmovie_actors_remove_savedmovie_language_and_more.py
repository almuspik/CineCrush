# Generated by Django 5.0 on 2025-07-24 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savedmovie',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='savedmovie',
            name='language',
        ),
        migrations.RemoveField(
            model_name='savedmovie',
            name='runtime',
        ),
        migrations.AddField(
            model_name='savedmovie',
            name='category',
            field=models.CharField(choices=[('Movie', 'Movie'), ('Anime', 'Anime'), ('TV Series', 'TV Series')], default='Movie', max_length=20),
        ),
    ]
