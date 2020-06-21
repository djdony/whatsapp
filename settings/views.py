from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from settings.forms import CompanyForm
from settings.models import Company
from django.views.generic import ListView, CreateView, DeleteView, UpdateView


def index(request):
    return render(request, 'home.html')


class CompanyUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'partials/form.html'
    slug_field = 'slug'
    success_url = reverse_lazy('company')
    success_message = 'Data Updated successfully.'


class CompanyAdd(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CompanyForm
    template_name = 'partials/form.html'
    success_url = reverse_lazy('company')
    success_message = 'Data Inserted successfully.'

    def form_valid(self, form):
        company = form.save()
        company.users.add(self.request.user)
        return super(CompanyAdd, self).form_valid(form)


class CompanyList(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'company.html'
    context_object_name = 'companies'

    def get_queryset(self):
        return Company.objects.filter(users__exact=self.request.user, status__exact=1)


@login_required
def company_delete(request, slug):
    user_company = get_object_or_404(Company, slug=slug, users=request.user)
    user_company.status = 0
    user_company.save()
    messages.success(request, 'Data deleted successfully.')
    return CompanyList.as_view()(request)
