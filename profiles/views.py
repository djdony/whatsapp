from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.safestring import mark_safe

from .forms import UserRegisterForm, UserLoginForm, UserProfileForm, ChangePassword
from settings.forms import CompanyForm
from .models import Profile
from settings.models import Company
from django.forms.utils import ErrorList


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
def company_edit(request, slug):
    company = get_object_or_404(Company, slug=slug, users=request.user)
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, error_class=DivErrorList, instance=company)
        if form.is_valid():
            form.save()

            messages.success(request, 'Data inserted successfully.')
            return redirect('company')
        else:
            messages.error(request, 'Please correct the error below.')

    form = CompanyForm(instance=company)
    return render(request, 'partials/form.html', {'form': form})


@login_required
def company_add(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, error_class=DivErrorList)
        if form.is_valid():
            company = form.save()
            company.users.add(request.user)
            messages.success(request, 'Data inserted successfully.')
            return redirect('company')
    else:
        form = CompanyForm()
    return render(request, 'partials/form.html', {'form': form})


@login_required
def company(request):
    companies = Company.objects.filter(users__exact=request.user, status__exact=1)
    return render(request, 'company.html', context={'companies': companies})


@login_required
def company_delete(request, slug):
    user_company = get_object_or_404(Company, slug=slug, users=request.user)
    user_company.status=0
    user_company.save()
    messages.success(request, 'Data deleted successfully.')
    return company(request)


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


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
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
            return redirect('profile')
    else:
        form = UserLoginForm()
    return render(request, 'auth/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')
