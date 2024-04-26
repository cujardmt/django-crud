from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import TravelerForm
from .models import Traveler


# Home Page - list all travellers
@login_required()
def home(request):
    records = Traveler.objects.all()
    context = {'records': records}
    return render(request, 'tbs/tbs-dash.html', context)

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
    return render(request, 'tbs/create-travel-request.html', context)

# read single travel request
@login_required()
def readTravelRequest(request, pk):
    traveler = Traveler.objects.get(id=pk)
    context = {'traveler': traveler}
    return render(request, 'tbs/read-travel-request.html', context)


# update travel requests
@login_required()
def updateTravelRequest(request, pk):
    traveler = Traveler.objects.get(id=pk)
    form = TravelerForm(instance=traveler)
    
    if request.method == 'POST':
        form = TravelerForm(request.POST, instance=traveler)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record was updated!")
            return redirect("dashboard")
        
    context = {'form':form}
    return render(request, 'trs/update-travel-request.html', context)


# delete
@login_required()
def deleteTravelRequest(request, pk):
    pass

