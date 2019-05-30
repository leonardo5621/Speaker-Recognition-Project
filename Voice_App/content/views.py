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


class PostCreateView(LoginRequiredMixin, CreateView, UserPassesTestMixin):
    model = News
    fields = ['title','text_body']
    success_url='/'

    def form_valid(self,form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
    
    def test_func(self):
        if self.request.user == 'leonardo': ##NOME DO USUARIO PRINCIPAL
            return True
        return False

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    fields = ['title','text_body']
    success_url = '/'
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        model = self.get_object()
        if self.request.user == model.author:
            return True
        return False

class PostDetailView(DetailView):
    model = News

class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = News
    success_url='/'
    def test_func(self):
        model = self.get_object()
        if self.request.user == model.author:
            return True
        return False

#class PostListView(ListView, LoginRequiredMixin, UserPassesTestMixin):
#    model = News
#    template_name = 'content/'
#    context_object_name = ''

