from django.contrib import admin 
from django.urls import path, include 
from . import views

urlpatterns = [
    path('login', views.login,name='login'),
    path('singup',views.sing_up,name='singup'),
    path('',views.home,name='home'),
    path('home',views.index1,name='index1'),
    path('logout', views.log_out,name='log_out'),
]
