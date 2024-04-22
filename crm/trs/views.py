from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# - Home Page
def home(request):
    return render(request, 'trs/index.html')


def createTravelRequest(request):
    return render(request, 'trs/create-travel-request.html')

def readTravelRequest(request):
    return render(request, 'trs/read-travel-request.html')

def updateTravelRequest(request):
    return render(request, 'trs/update-travel-request.html')

def deleteTravelRequest(request):
    pass