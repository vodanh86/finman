from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from api.models import Company

class UserTestCase(TestCase):
    def setUp(self):
        Company.objects.create(name="lion", sound="roar")
        Company.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Company.objects.get(name="lion")
        cat = Company.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')