from django.db import models
# from django.contrib.auth.models import User
import datetime as dt

#class for image category below
class Tags(models.Model):
    name = models.CharField(max_length = 30)
    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()

class Meta:
        ordering =['name']