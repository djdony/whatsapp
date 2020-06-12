from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from .forms import UserRegisterForm, UserLoginForm


def index(request):
    return render(request, 'home.html')


def profile(request):
    return render(request, 'profile.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if form.cleaned_data['role'] == 'company':
                group = Group.objects.get(name='Company')
                group.user_set.add(user)
            login(request, user)
            messages.success(request, 'Success')
            return redirect('profile')
        else:
            messages.error(request, 'Error')
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'auth/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')