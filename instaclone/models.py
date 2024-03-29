from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    profile_picture = models.ImageField(upload_to='images/')
    bio = models.TextField(max_length=500)
    name = models.CharField( max_length=120)
    location = models.CharField(max_length=60)
    email = models.EmailField(null=True)

    def save_image(self):
        self.save()

    def save_profile(self):
        self.save()
        
    def delete_image(self):
        self.delete()
    
    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.first_name
    
    @classmethod
    def search_by_title(cls,search_term):
        instaclone = cls.objects.filter(title__icontains=search_term)
        return instaclone

class Post(models.Model):
   
    image = models.ImageField(upload_to='posts/')
    user = models.ForeignKey(User, on_delete = models.CASCADE,default='',related_name='user_post')
    profile = models.ForeignKey('Profile', on_delete = models.CASCADE,default='',related_name='user_profile')
    caption = models.CharField(max_length=250)
    name = models.CharField(max_length=250, default='')
    # created_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey("Image", on_delete=models.CASCADE, null=True)
    comment = models.TextField()

class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/')
    imageName = models.CharField(max_length = 30)
    imageCaption = models.TextField()
    # comments = models.ForeignKey(Comments, on_delete = models.CASCADE, null = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    created = models.DateTimeField(auto_now_add = True, null = True)