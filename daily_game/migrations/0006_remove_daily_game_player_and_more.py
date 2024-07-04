# Generated by Django 4.2 on 2024-06-25 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('daily_game', '0005_alter_daily_game_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daily_game',
            name='player',
        ),
        migrations.RemoveField(
            model_name='daily_game',
            name='score_conundrum',
        ),
        migrations.RemoveField(
            model_name='daily_game',
            name='score_letters',
        ),
        migrations.RemoveField(
            model_name='daily_game',
            name='score_numbers',
        ),
        migrations.RemoveField(
            model_name='daily_game',
            name='score_total',
        ),
        migrations.CreateModel(
            name='Plays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_letters', models.IntegerField(null=True)),
                ('score_numbers', models.IntegerField(null=True)),
                ('score_conundrum', models.IntegerField(null=True)),
                ('score_total', models.IntegerField(null=True)),
                ('game_played', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='daily_game.daily_game')),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
