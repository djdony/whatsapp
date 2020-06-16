from django import forms
from .models import Company, CompanyType, City


class CompanyForm(forms.ModelForm):
    error_css_class = 'error'
    CHOICES = [('customer', 'Customer'), ('company', 'Company')]
    name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    whatsapp = forms.CharField(label='Whatsapp', widget=forms.TextInput(attrs={'class': 'form-control'}))
    www = forms.CharField(label='WWW', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.ModelChoiceField(label='City', queryset=City.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control'}))
    company_type = forms.ModelChoiceField(label='Company Type', queryset=CompanyType.objects.all(),
                                          widget=forms.Select(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    logo = forms.ImageField(label='Logo', required=False)

    class Meta:
        model = Company
        fields = ('name', 'address', 'whatsapp', 'www', 'city', 'company_type', 'email', 'logo')
