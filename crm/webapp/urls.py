from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signin', views.signIn, name="signin"),
    path('signup', views.signUp, name="signup"),
    path('signout', views.signOut, name="signout"),
    
    # CRUD
    path('dashboard', views.dashboard, name="dashboard"),
    path('create-record', views.createRecord, name="create-record"),
    path('update-record/<int:pk>', views.updateRecord, name='update-record'),
    path('record/<int:pk>', views.readRecord, name="view-record"),
    path('delete-record/<int:pk>', views.deleteRecord, name="delete-record"),

]