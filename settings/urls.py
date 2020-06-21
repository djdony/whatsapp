from django.urls import path
from .views import index, company_delete, CompanyList, CompanyAdd, CompanyUpdate

urlpatterns = [
    path('', index, name='home'),
    path('company/', CompanyList.as_view(), name='company'),
    path('company/<slug:slug>/edit', CompanyUpdate.as_view(), name='company_edit'),
    path('company/<slug:slug>/delete', company_delete, name='company_delete'),
    path('company/add', CompanyAdd.as_view(), name='company_add'),
    ]