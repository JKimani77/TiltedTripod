from django.db import models
# from django.contrib.auth.models import User
import datetime as dt

#class for image category below
class Tags(models.Model):
    name = models.CharField(max_length = 30)
    def save_tag(self):
        self.save()
    def delete_tag(self):
        self.delete()

    @classmethod
    def get_tag_by_ID(cls, id):
        cat = Tags.objects.get(pk=id)
        return cat
    
    def update_tag(self, updated_category):
        self.image_category = updated_category
        self.save()

class Meta:
        ordering =['name']

class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=30)
    image = models.ImageField(upload_to='gallery/', blank=True)
    category = models.ForeignKey(Tags, on_delete=models.CASCADE)
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()

    # @classmethod  
    # def get_image_by_id(cls, id):
    #     image = cls.objects.filter(id=id).all()
    #     return image
        
    def update_image(self,image_name, image_description):
        self.image_name = image_name
        self.image_description = image_description
        self.save()
    
    