from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth.models import User,auth

# Create your views here.
def result(request):
    username=request.user
    user=User.objects.filter(username=username).first()
    obj=user.profile
    return render(request,'result.html',{'user':obj})
