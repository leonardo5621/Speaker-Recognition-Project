from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('create_post/', views.PostCreateView.as_view(), name='create-post'),
        path('delete_post/<int:pk>/', views.PostDeleteView.as_view(), name='delete-post'),
        path('update_post/<int:pk>', views.PostUpdateView.as_view(), name='update-post'),
        path('post/<int:pk>', views.PostDetailView.as_view(), name='detail-post')
        ]

