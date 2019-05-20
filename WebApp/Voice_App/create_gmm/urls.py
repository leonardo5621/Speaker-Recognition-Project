from django.urls import path
from . import views

urlpatterns = [
        path('createmodel', views.ModelCreateView.as_view(), name="create-model"),
        ]

