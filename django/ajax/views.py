from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mainView(request): ##  this is main Ajax page with Javascript
  return render(request, 'ajax/main.html')

def mainCalc(request): ##  this is blank page only for sending server reponse to Ajax from main.html
  mainl1 = request.GET.get('l1','Nothing')
  return HttpResponse(f'{mainl1}')
  
