from .models import Image
from django.shortcuts import render

# Create your views here.
def index(request):
    '''
    Function that displays the photos
    '''
    gallery=Image.objects.all()
    return render(request,'index.html', {'gallery':gallery})
