from django.shortcuts import render

from django.views.generic import ListView, CreateView  # views to show and upload images
from django.urls import reverse_lazy   # handle automatic redirect after issuing form
from .forms import PostForm		# form to upolad image
from .models import Post


# Create your views here.
count = 0

def mainView(request):
  global count
  count += 1
  return render(request, 'posts/main.html', {'minutes': count})
