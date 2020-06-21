from django.urls import path
from .views import user_login, user_logout, profile, change_password, Register

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('change_password/', change_password, name='change_password'),
    ]