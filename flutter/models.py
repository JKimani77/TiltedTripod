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

class Meta:
        ordering =['name']

class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=30)
    image = models.ImageField(upload_to='gallery/', blank=True)
    category = models.ForeignKey(Tags, on_delete=models.CASCADE)
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    