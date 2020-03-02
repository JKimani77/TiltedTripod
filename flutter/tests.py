from django.test import TestCase
from .models import Image, Tags, Meta

class ImageTestClass(TestCase):
    '''
    Test case for model image
    '''
    def setUp(self):
        self.any_category = Tags(name = 'FOOD')
        self.any_image = Image(image_name = 'TOMATOES', image_description = 'a tomato tomattoed', image = '/path.image.png', category =self.any_category)


    def test_search_by_category(self):
        self.any_category.save_tag()
        self.any_image.save_image()
        images = self.any_image.search_by_tag('FOOD')
        self.assertTrue(len(images)>0)