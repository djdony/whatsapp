
from django import forms
from .models import Company


class CompanyForm(forms.Form):
    CHOICES = [('customer', 'Customer'), ('company', 'Company')]
    name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    whatsapp = forms.CharField(label='Whatsapp', widget=forms.TextInput(attrs={'class': 'form-control'}))
    www = forms.CharField(label='WWW', widget=forms.TextInput(attrs={'class': 'form-control'}))
    city_id = forms.ChoiceField(label='City', widget=forms.Select(attrs={'class': 'form-control'}))
    company_type = forms.ChoiceField(label='Company Type', widget=forms.Select(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    logo = forms.ImageField(label='Logo')

    class Meta:
        model = Company
        fields = ('first_name', 'last_name', 'address', 'whatsapp')