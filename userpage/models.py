from django.db import models
from django.contrib.auth.models import User,auth
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import datetime
from django.conf import settings
# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    caption=models.CharField(max_length=20)
    image=models.ImageField(upload_to='user_image',blank=True)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.user)