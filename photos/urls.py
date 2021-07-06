from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'^search/',views.search_results,name='results'),
    url(r'^nature/$', views.nature, name = 'nature'),
    url(r'^fashion/$', views.fashion, name = 'fashion'),
    url(r'^food/$', views.food, name = 'food'),
    url(r'^animals/$', views.animals, name = 'animals'),
    url(r'^single_image/<int:image_1', views.image, name='image')

]


