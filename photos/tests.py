from django.test import TestCase
from .models import Image

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
       
        self.new_image= Image(name = 'me',description = 'This is a random post')
        self.new_image.save()


