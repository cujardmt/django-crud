from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # home page will display a dashboard
    path('', views.home, name="tbs-dash"),
    
    # CRUD
    path('create-travel-request', views.createTravelRequest, name="create-travel-request"),
    path('read-travel-request/<int:pk>', views.readTravelRequest, name="read-travel-request"),
    path('update-travel-request/<int:pk>', views.updateTravelRequest, name="update-travel-request"),
    # path('update-record/<int:pk>', views.updateRecord, name='update-record'),
    # path('record/<int:pk>', views.readRecord, name="view-record"),
    # path('delete-record/<int:pk>', views.deleteRecord, name="delete-record"),

]

# https://stackoverflow.com/questions/68490434/using-project-level-templates-django