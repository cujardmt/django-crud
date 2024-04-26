from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signin', views.signIn, name="signin"),
    path('signup', views.signUp, name="signup"),
    path('signout', views.signOut, name="signout"),
    path('dashboard', views.dashboard, name="dashboard"),
    
]