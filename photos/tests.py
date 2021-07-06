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


class LocationTestClass(TestCase):
    def setUp(self):
       
        self.loc= Location(name = 'Africa')
        self.loc.save()

    def test_get_locations(self):
        location=Location.get_locations(self.loc.id)
        self.assertTrue(len(location) == 1)

    def test_update_location(self):
        location = Location.get_locations(self.loc.id)
        location.update_location('Africa')
        location = Location.get_locations(self.loc.id)
        self.assertTrue(location.name == 'Africa')

    def test_save_location(self):
        self.loc.save_location()
        location=Location.objects.all()
        self.assertTrue(len(location)>0)

    def test_delete_location(self):
        self.loc.save_location()
        self.loc.delete_location()
        location =Location.objects.all()
        self.assertTrue(len(location) == 0)

class CategoryTestClass(TestCase):
    def setUp(self):
       
        self.category= Category(name = 'Food')
        self.category.save()
    
    def test_get_category_id(self):
        category=Category.get_category_id(self.category.id)
        self.assertTrue(len(category) == 1)

    def test_update_category(self):
        category = Category.get_category_id(self.category.id)
        category.update_category('Food')
        category = Category.get_category_id(self.category.id)
        self.assertTrue(category.name =='Food')

    def test_save_category(self):
        self.category.save_category()
        category=Category.objects.all()
        self.assertTrue(len(category)>0)

    def test_delete_category(self):
        self.category.save_category()
        self.category.delete_category()
        category =Category.objects.all()
        self.assertTrue(len(category) == 0)
    





