from django.urls import path
from . import views

urlpatterns = [
        path('', views.Home, name="home"),
        path('About/', views.AboutPage, name="about"),
        path('signup/', views.register, name="signup"),
        path('profile/', views.profile, name='profile'),
        ]
