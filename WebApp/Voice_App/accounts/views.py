from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

class SignUp(generic.CreateView):
    form_class= UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

def Home(request):
    return render(request, 'accounts/home_template.html')

def AboutPage(request):
    return render(request, 'accounts/About.html')

@login_required
def profile(request):
    return render(request, 'accounts/loggedIn.html')
