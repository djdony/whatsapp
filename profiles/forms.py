from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from django import forms
from .models import Profile


class UserLoginForm(AuthenticationForm):
    error_css_class = 'error'
    username = forms.CharField(label=_('Login'), widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    error_css_class = 'error'
    CHOICES = [('customer', 'Customer'), ('company', 'Company')]
    username = forms.CharField(label=_('Login'), help_text='Maximum 150 chars',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label=_('E-mail'), widget=forms.EmailInput(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(choices=CHOICES, widget=forms.Select())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ChangePassword(PasswordChangeForm):
    error_css_class = 'error'
    old_password = forms.CharField(label=_('Old Password'), widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label=_('New Password'), widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        field_order = ['old_password', 'new_password1', 'new_password2']


class UserProfileForm(forms.ModelForm):
    error_css_class = 'error'
    first_name = forms.CharField(label=_('First Name'), widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label=_('Last Name'), widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label=_('Address'), widget=forms.TextInput(attrs={'class': 'form-control'}))
    whatsapp = forms.CharField(label=_('Whatsapp'), widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'address', 'whatsapp')