from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique='True')

    class Meta:
        ordering = ["name"]

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self, update):
        self.name = update
        self.save()

    @classmethod
    def get_category_id(cls,id):
        category = Category.objects.get(pk = id)
        return category

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=60,unique=True)

    class Meta:
        ordering = ["name"]

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    def __str__(self):
        return self.name


class Image(models.Model):
    name=models.CharField(max_length=80)
    description=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='media/')
    location = models.ForeignKey(Location, related_name='location', on_delete=models.DO_NOTHING, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.DO_NOTHING, null=True, blank=True)


    class Meta:
        ordering=["pub_date"]
    

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    @classmethod
    def update_image(cls,id,value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def retrieve_images(cls):
        images=cls.objects.all()
        return images
    
    @classmethod
    def get_image_by_id(cls):
        images=cls.objects.get(pk=id)
        return images
    
    @classmethod
    def search_image(cls,category):
        image=cls.objects.filter(category__name__icontains=category)
        return image

    
    def __str__(self):
        return self.name
