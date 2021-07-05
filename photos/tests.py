from django.test import TestCase
from .models import Image

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
       
        self.new_image= Image(name = 'me',description = 'This is a random post')
        self.new_image.save()

    def test_retrieve_images(self):
        self.new_image.save_image()
        retrieve_image=Image.retrieve_images()
        print(retrieve_image)
        self.assertTrue(len(retrieve_image)==1)

    


