from django.urls import path
from .views import index, user_login, user_logout, register, profile, change_password, company, company_edit, \
    company_add, company_delete

urlpatterns = [
    path('', index, name='home'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('change_password/', change_password, name='change_password'),
    path('company/', company, name='company'),
    path('company/<slug:slug>/edit', company_edit, name='company_edit'),
    path('company/<slug:slug>/delete', company_delete, name='company_delete'),
    path('company/add', company_add, name='company_add'),
    ]