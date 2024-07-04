from django.contrib import admin
from django.urls import path
from daily_game import views

app_name = 'daily_game'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('letters/', views.LettersView.as_view(), name="letters"),
    path('numbers/', views.NumbersView.as_view(), name="numbers"),
    path('word/', views.ConunView.as_view(), name="word"),
    path('results/', views.results_view, name="results"),
    path('gamelist/', views.GameListView.as_view(), name="gamelist"),
    path('gamedetail/<int:pk>', views.GameDetailView.as_view(), name="gamedetail"),
]