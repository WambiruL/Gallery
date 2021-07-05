from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'^$',views.image, name='image'),
    url(r'^search/',views.search_results,name='results')
]


