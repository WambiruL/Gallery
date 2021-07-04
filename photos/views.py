from .models import Image, Location
from django.shortcuts import render

# Create your views here.
def index(request):
    '''
    Function that displays all the photos
    '''
    gallery=Image.objects.all()
    location=Location.get_locations()
    return render(request,'index.html', {'gallery':gallery},{'locations':location})
