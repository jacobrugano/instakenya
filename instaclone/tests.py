from django.test import TestCase
from .models import Profile,Post

# Create your tests here.
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Profile(user=1,profile_picture='image',bio='jacob',name='jacobm',location='kenya',email='jacobrugano@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.user,Profile))