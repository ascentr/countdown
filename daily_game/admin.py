from django.contrib import admin
from daily_game.models import Daily_Game, Plays

class Daily_GameAdmin(admin.ModelAdmin):
  list_display = ['letters' , 'date']

class PlaysAdmin(admin.ModelAdmin):
  list_display = ['game', 'player', 'score_total']


admin.site.register(Daily_Game, Daily_GameAdmin)
admin.site.register(Plays, PlaysAdmin)