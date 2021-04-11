from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

##  MESSAGE ADDING PAGE FROM 101(8.1.12)

##  MAIN CHAT PAGE WITH LOGIN FORM LINK
def index(request):
    return render(request, 'index.html')

##  LOGIN PAGE FROM 101(8.1.11)
def log_in(request):
    #    return redirect('./alert')
    log_info = 'Please type username and password'
    if request.method == 'POST':
        ############################  GENIUS!!  ####  DEFAULT request.GET.get  ########
        log_info = f"{request.POST.get('username', 'This')} is not valid username."
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            print("----VALID----")
            login(request, form.get_user())
            
            return redirect('./')
    
    return render(request, 'login.html', {'form': AuthenticationForm(), 'info': log_info})

def alert(request):
    return HttpResponse("ALERT")
    
