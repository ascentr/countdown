from django.contrib import admin
from django.urls import path , include
from daily_game import views




urlpatterns = [
    path('', views.IndexView.as_view(), name='index') , 
    path('admin/', admin.site.urls),
    path('daily_game/', include('daily_game.urls', namespace="daily_game")),
    path('registration/', include('django.contrib.auth.urls')),
    path('registration/', include('registration.urls', namespace="register")),
]