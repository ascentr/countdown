from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView, ListView, DetailView 
import datetime
from datetime import date
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from daily_game.models import *
from daily_game.utils import generate_game
from django.contrib.auth.models import User

class IndexView(TemplateView):

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['scores'] = Plays.objects.all().order_by('-score_total')[:5]
        return context

    template_name = 'daily_game/daily_index.html'


class LettersView(TemplateView):
    template_name = 'daily_game/daily_letters.html'

class NumbersView(TemplateView):
    template_name = 'daily_game/daily_numbers.html'

class ConunView(TemplateView):
    template_name ='daily_game/daily_word.html'


def results_view(request):
    game_today = Daily_Game.objects.get(date=datetime.date.today())
    game_played = game_today
    player = request.user
    game_scores = Plays.objects.filter(game=game_played)

    if game_today:
        if request.method == "POST":
            score_letters = request.POST["letScore"]
            score_numbers = request.POST["numScore"]
            score_conundrum = request.POST["conScore"]    
            score_total = request.POST["total"] 

            new_scores = Plays(
                game=game_played, 
                player=player, 
                score_letters=int(score_letters), 
                score_numbers=int(score_numbers), 
                score_conundrum=int(score_conundrum), 
                score_total=int(score_total)
            )
            new_scores.save()

    scores = Plays.objects.all().order_by('-score_total')
    context = {'scores' : scores }

    return render(request, 'daily_game/results.html' , context)


class GameListView(ListView):
    context_object_name = "games"
    model = Daily_Game
    template_name = "daily_game/daily_game_list.html"

    def get_queryset(self):
        queryset = super().get_queryset().annotate(num_plays=Count('game_played'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['games'] = self.get_queryset()
        return context


class GameDetailView(DetailView):
    model = Daily_Game

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        game = self.get_object()
        context['game'] = game
        context['scores'] = Plays.objects.filter(game=game).order_by('-score_total')
        return context

