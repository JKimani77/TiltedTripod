from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Tags,Image
import datetime as dt

def index(request):
    images = Image.get_images()
    #  locations = Location.objects.all()
    return render(request,'home.html', {"images":images})

def search_image(request):
    if 'image' in request.GET and request.GET['image']:
        search_word = request.GET.get('image')
        search = Image.search_by_tag(search_word)
        wurd =f"{search_word}"
        return render(request, 'search.html',{"wurd":wurd, "images":search})
    
    else:
        message= "You have not searched anything yet.."
        return render(request, 'search.html', {"message":message})