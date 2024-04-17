from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CreateUserForm, LoginForm, UpdateRecordForm, CreateRecordForm
from .models import Record

# - Home Page
def home(request):
    return render(request, 'index.html')

# Sign In or Log In
def signIn(request):
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        # authenticate only if the form is valid
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            # if user exist,
            # redirect to the dashboard
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            
    context = {'form': form}    
    return render(request, 'signIn.html', context=context)


# Sign Up or Register
def signUp(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        # save only if the form is valid
        # then redirect to /signin page
        if form.is_valid():
            form.save()
            return redirect('signin')
        
    context = {'form': form}
    return render(request, 'signUp.html', context)    


# Sign Out
def signOut(request):
    logout(request)
    # redirect to sign on successful log out
    return redirect('signin')


# Dashboard
# Display all existing records (for now)
# route to settings.LOGIN_URL if not authenticated
@login_required()
def dashboard(request):
    records = Record.objects.all()
    context = {'records': records}
    return render(request, 'dashboard.html', context)


@login_required()
def createRecord(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record was created!")
            return redirect("dashboard")

    context = {'form': form}
    return render(request, 'create-record.html', context)


@login_required()
def readRecord(request, pk):
    record = Record.objects.get(id=pk)
    context = {'record': record}
    return render(request, 'view-record.html', context)


@login_required()
def updateRecord(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record was updated!")
            return redirect("dashboard")
        
    context = {'form':form}
    return render(request, 'update-record.html', context=context)
    

@login_required()
def deleteRecord(request, pk):
    record = Record.objects.get(id=pk)
    
    # TODO Exception handling?
    record.delete()
    messages.success(request, "Your record was deleted!")
    return redirect("dashboard")
    