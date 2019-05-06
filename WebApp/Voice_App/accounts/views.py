from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignup

def register(request):
    if request.method == 'POST':
        form = UserSignup(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta Criada Com Sucesso!')
            return redirect('home')
    else:
        form = UserSignup()

    return render(request, 'accounts/signup.html', {'form': form})

def Home(request):
    return render(request, 'accounts/home_template.html')

def AboutPage(request):
    return render(request, 'accounts/About.html')

@login_required
def profile(request):
    return render(request, 'accounts/loggedIn.html')
