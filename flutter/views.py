from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Tags
import datetime as dt

def index(request):
    # images = Image.get_images()
    return render(request,'home.html')