from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import TravelerForm
from .models import Traveler


# - Home Page
@login_required()
def home(request):
    return render(request, 'trs/index.html')

# create a travel request
@login_required()
def createTravelRequest(request):
    form = TravelerForm()
    
    if request.method == 'POST':
        form = TravelerForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Your record was saved successfully.")
            return redirect("dashboard")
        
    context = {'form': form}
    return render(request, 'trs/create-travel-request.html', context)

# read single travel request
@login_required()
def readTravelRequest(request):
    return render(request, 'trs/read-travel-request.html')

# update travel requests
@login_required()
def updateTravelRequest(request):
    return render(request, 'trs/update-travel-request.html')

# delete
@login_required()
def deleteTravelRequest(request):
    pass