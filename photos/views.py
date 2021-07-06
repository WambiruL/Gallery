from .models import Image, Location, Category
from django.shortcuts import render
from django.http import Http404
#from django.views.generic import DetailView

# Create your views here.
def index(request):
    '''
    Function that displays all the photos
    '''
    images=Image.retrieve_images()
    location=Location.get_locations()
    return render(request,'index.html', {'images':images,'location':location})

def image(request,image_id):
    try:
        image = Image.objects.get(pk = image_id)
    except Image.DoesNotExist:
        raise Http404()
    return render(request,"single_image.html", {"image":image})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

    return render(request, 'search.html',{"message":message,"images": searched_images})

def nature(request):
    nature_category = Category.objects.get(pk=2)
    nature = Image.objects.filter(category=nature_category)
    return render(request,'nature.html', {'nature':nature})

def fashion(request):
    fashion_category = Category.objects.get(pk=4)
    fashion = Image.objects.filter(category=fashion_category)
    return render(request,'fashion.html', {'fashion':fashion})

def food(request):
    food_category = Category.objects.get(pk=3)
    food = Image.objects.filter(category=food_category)
    return render(request,'food.html', {'food':food})

def animals(request):
    animals_category = Category.objects.get(pk=1)
    animals = Image.objects.filter(category=animals_category)
    return render(request,'animals.html', {'animals':animals})


#class imagedisplay(DetailView):
 #  model = Image
  # template_name = 'index.html'
   #context_object_name = 'image'

