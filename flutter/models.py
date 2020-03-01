from django.db import models
from django.contrib.auth.models import User
import datetime as dt

#class for image category below
class Tags(models.Model):
    name = models.Charfield(max_length = 30)