from django.test import TestCase
from .models import Image, Location, Category

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

    def test_save_image(self):
        self.new_image.save_image()
        images= Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_image(self):
        self.new_image.save_image()
        self.new_image.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(image) == 0)

    def test_update_image(self):
        images = Image.get_image_by_id(self.new_image.id)
        images.update_image('Africa')
        images = Image.get_image_by_id(self.new_image.id)
        self.assertTrue(images.id ==1)

    def test_get_image_by_id(self):
        images= Image.get_image_by_id(self.new_image.id)
        self.assertTrue(len(images) == 1)

    def test_search_image(self):
        images = Image.search_image('fashion')
        self.assertTrue(len(images)>0)


