from django.urls import path
from .views import index, user_login, user_logout, register, profile, change_password, company

urlpatterns = [
    path('', index, name='home'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('change_password/', change_password, name='change_password'),
    path('company/', company, name='company'),
    ]