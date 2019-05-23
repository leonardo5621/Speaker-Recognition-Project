import json
import pandas as pd
from django_tables2.tables import Table
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignup, UserUpdateForm, ProfileUpdateForm
#from .models import Product

def register(request):
    if request.method == 'POST':
        form = UserSignup(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta Criada Com Sucesso!')
            return redirect('login')
    else:
        form = UserSignup()
    return render(request, 'accounts/signup.html', {'form': form})


def AboutPage(request):
    return render(request, 'accounts/About.html')

#def products(request):
#    queryset = Product.objects.all()
#    names = [obj.name for obj in queryset]
#    prices = [int(obj.price) for obj in queryset]
#
#    context = {
#        'names': json.dumps(names),
#        'prices': json.dumps(prices),
#    }
#    return render(request, 'chart/products.html', context)

@login_required
def profile(request):
    csvfile = 'DistFrame.csv'
    data = pd.read_csv(csvfile)
    data_h = data.to_html(classes="table table-striped table-sm", justify="center")
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                request.FILES,
                instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Conta Atualizada Com Sucesso!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
            'u_form': u_form,
            'p_form': p_form,
            'data': data_h
            }

    return render(request, 'accounts/loggedIn.html', context)

