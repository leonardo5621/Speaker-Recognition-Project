from django.urls import path
from . import views

urlpatterns = [
        path('createmodel', views.ModelCreateView.as_view(), name="create-model"),
        path('update/<int:pk>/', views.ModelUpdateView.as_view(), name="update-model"),
        path('<int:pk>/', views.ModelDetailView.as_view(), name="detail-model")
        ]

