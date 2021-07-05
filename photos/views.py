from .models import Image, Location
from django.shortcuts import render

# Create your views here.
def index(request):
    '''
    Function that displays all the photos
    '''
    images=Image.retrieve_images()
    location=Location.get_locations()
    return render(request,'index.html', {'images':images,'location':location})

