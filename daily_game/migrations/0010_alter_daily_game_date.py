# Generated by Django 4.2 on 2024-06-29 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_game', '0009_remove_plays_game_played_plays_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_game',
            name='date',
            field=models.DateField(),
        ),
    ]