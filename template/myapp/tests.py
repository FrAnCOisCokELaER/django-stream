from django.test import TestCase
from .views import *
from template.mongoconnector import insertdocument


# Create your tests here.
class Base64TestCase(TestCase):

    def test_toto(self):
        self.assertEqual(encode('toto'),"dG90bw==")

    #def test_mongo_insertion(self):
    #    mydocument = {"app": "myapp", "service": "encoder"}
    #    insertdocument(mydocument, 'myapp')
