from django.urls import path
from . import views

urlpatterns = [
        path('', views.Home, name="homeview"),
        path('About/', views.AboutPage, name="about"),
        path('signup/', views.SignUp.as_view(), name="signup"),
        path('profile/', views.profile, name='profile')
        ]
