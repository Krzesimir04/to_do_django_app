from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('register',register,name='register'),
    path('login',loginFunction,name='login'),
    path('logout',logoutFunction,name='logout'),
]