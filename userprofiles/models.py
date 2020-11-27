from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User,auth
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name=models.CharField(max_length=20,blank=True)
    profile_image = models.ImageField(upload_to='avatars', default='avatars/2_101.png')
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=20, blank=True)
    status=models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=20, blank=True)
