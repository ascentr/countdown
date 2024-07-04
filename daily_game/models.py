from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Daily_Game(models.Model):
    letters = models.CharField(max_length=9)
    numbers = models.CharField(max_length=20)
    num_target = models.IntegerField(default=150)
    conundrum = models.CharField(max_length=9)
    # date = models.DateField(auto_now=True, auto_now_add=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.letters 


class Plays(models.Model):
    game = models.ForeignKey(Daily_Game, related_name="game_played", on_delete=models.CASCADE, null=True)
    player = models.ForeignKey(User, related_name="player", on_delete=models.CASCADE, null=True)
    score_letters = models.IntegerField(null=True)
    score_numbers = models.IntegerField(null=True)
    score_conundrum = models.IntegerField(null=True)
    score_total = models.IntegerField(null=True)

    def __int__(self):
        return self.game

    class Meta:
            verbose_name_plural = "plays"
