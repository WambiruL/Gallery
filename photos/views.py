from .models import Image
from django.shortcuts import render

# Create your views here.
def gallery(request):
    '''
    Function that displays the photos
    '''
    gallery=Image.objects.all()
    return render(request,'gallery.html', {'gallery':gallery})
