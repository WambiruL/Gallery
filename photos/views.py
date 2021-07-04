from .models import Image, Location
from django.shortcuts import render

# Create your views here.
def index(request):
    '''
    Function that displays all the photos
    '''
    images= Image. retrieve_images()
    ctx={
        "images":images
    }
    location=Location.get_locations()
    return render(request,'index.html', ctx,{'locations':location})

