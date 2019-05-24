from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import News

def home(request):
    context = {
        'News': News.objects.all()
    }
    return render(request, 'content/home.html', context)


