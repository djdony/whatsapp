from django import forms
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from .models import Company, CompanyType, City


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return mark_safe(''.join(['<div class="alert alert-danger" role="alert">%s</div>' % e for e in self]))


class CompanyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs_new = {'error_class': DivErrorList}
        kwargs_new.update(kwargs)
        super(CompanyForm, self).__init__(*args, **kwargs_new)
    name = forms.CharField(label=_('First Name'), widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label=_('Address'), widget=forms.TextInput(attrs={'class': 'form-control'}))
    whatsapp = forms.CharField(label=_('Whatsapp'), widget=forms.TextInput(attrs={'class': 'form-control'}))
    www = forms.CharField(label=_('WWW'), required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.ModelChoiceField(label=_('City'), queryset=City.objects.all(),
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    company_type = forms.ModelChoiceField(label=_('Company Type'), queryset=CompanyType.objects.all(),
                                          widget=forms.Select(attrs={'class': 'form-control'}))
    email = forms.EmailField(label=_('E-mail'), widget=forms.EmailInput(attrs={'class': 'form-control'}))

    logo = forms.ImageField(label=_('Logo'), required=False)

    class Meta:
        model = Company
        fields = ('name', 'address', 'whatsapp', 'www', 'city', 'company_type', 'email', 'logo')
