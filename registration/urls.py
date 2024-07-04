from django.urls import path , include
from django.contrib.auth import views as auth_views
from . import views
    
app_name = 'registration'

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login") ,
    path('logout/', auth_views.LogoutView.as_view(), name="logout", kwargs={'next_page':'/'}),
    path('signup/', views.signup, name= "signup"),


    # path('login/', views.login, name="login"),
    # path('logout/', views.logout, name='logout'),
]    
    
