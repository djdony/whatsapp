from django.urls import path
from .views import index, user_login, user_logout, register, profile

urlpatterns = [
    path('', index, name='home'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    ]