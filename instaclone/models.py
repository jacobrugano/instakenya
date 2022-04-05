from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    profile_picture = models.ImageField(upload_to='images/')
    bio = models.TextField(max_length=500)
    name = models.CharField( max_length=120)
    location = models.CharField(max_length=60)
    