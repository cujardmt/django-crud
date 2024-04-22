from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# - Home Page
@login_required()
def home(request):
    return render(request, 'trs/index.html')

@login_required()
def createTravelRequest(request):
    return render(request, 'trs/create-travel-request.html')

@login_required()
def readTravelRequest(request):
    return render(request, 'trs/read-travel-request.html')

@login_required()
def updateTravelRequest(request):
    return render(request, 'trs/update-travel-request.html')

@login_required()
def deleteTravelRequest(request):
    pass