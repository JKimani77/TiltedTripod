from django.contrib import admin
from .models import Image, Tags, Meta

admin.site.register(Tags)
# admin.site.register(Meta)
admin.site.register(Image)
