from .models import Image, Location
from django.shortcuts import render
from django.http import Http404

# Create your views here.
def index(request):
    '''
    Function that displays all the photos
    '''
    images=Image.retrieve_images()
    location=Location.get_locations()
    return render(request,'index.html', {'images':images,'location':location})

def image(request,article_id):
    try:
        image = Image.objects.get(id = article_id)
    except Image.DoesNotExist:
        raise Http404()
    return render(request,"single_image.html", {"image":image})
