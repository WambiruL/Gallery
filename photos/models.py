from django.db import models

# Create your models here.
class Image(models.Model):
    name=models.CharField(max_length=80)
    description=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='Images/')

    class Meta:
        ordering=["pub_date"]

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    @classmethod
    def update_image(cls,id,value):
        cls.objetcs.filter(id=id).update(image=value)
    
    @classmethod
    def get_image_by_id(cls):
        images=cls.objects.get(pk=id)
        return images
    
    @classmethod
    def search_image(cls,category):
        image=cls.objects.filter(category__name__icontains=category)
        return image

    @classmethod
    def filter_by_location(cls,location):
        image_location=Image.objects.filter(location__name=location).all()
        return image_location

    
    def __str__(self):
        return self.name