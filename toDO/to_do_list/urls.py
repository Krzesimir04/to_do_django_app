from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('register',register,name='register'),
    path('login',loginFunction,name='login'),
    path('logout',logoutFunction,name='logout'),
    path('new',new,name='new'),
    path('edit/<str:pk>',edit,name='edit'),
    path('delete/<str:pk>',delete,name='delete'),
]