from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe

from .forms import UserRegisterForm, UserLoginForm, UserProfileForm, ChangePassword
from .models import Profile
from django.forms.utils import ErrorList
from django.views.generic import ListView, CreateView, DeleteView, UpdateView


def index(request):
    return render(request, 'home.html')


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return mark_safe(''.join(['<div class="alert alert-danger" role="alert">%s</div>' % e for e in self]))


@login_required
def profile(request):
    try:
        user_profile = request.user.profile
    except Profile.DoesNotExist:
        user_profile = Profile(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Data Updated successfully.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'partials/form.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePassword(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ChangePassword(request.user)
    return render(request, 'partials/form.html', {'form': form})


class Register(CreateView):
    form_class = UserRegisterForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = super(Register, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        if form.cleaned_data['role'] == 'company':
            group = Group.objects.get(name='Company')
            group.user_set.add()
        return user


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = UserLoginForm()
    return render(request, 'auth/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')
