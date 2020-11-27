from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import  Post
from accounts.views import logout_view
from userprofiles.models import Profile
from django.contrib.auth import logout
# Create your views here.
def post(request):
    if request.method=="POST":
        image=request.FILES.get("image")
        captions=request.POST.get("captions")
        user=request.user
        p=Post(user=user,caption=captions,image=image)
        p.save()
        return redirect("/userpage/post")
    else:
        posts=Post.objects.all()
        p={'posts':posts}
        return render(request,"post.html",p)
def mypost(request):
    if request.method=="POST":
        image=request.FILES.get("image")
        captions=request.POST.get("captions")
        user=request.user
        p=Post(user=user,caption=captions,image=image)
        p.save()
        return redirect("/userpage/mypost")
    else:
        posts=Post.objects.all().filter(user=request.user)
        p={'posts':posts}
        return render(request,"mypost.html",p)
def result(request):
    username=request.user
    user=User.objects.filter(username=username).first()
    obj=user.profile
    l=[]
    city=obj.city
    user_city=User.objects.all()
    for i in user_city:
        if i.profile.city==city and i!=user:
            l.append(i) 
    return render(request,'result.html',{'user':obj,'user_city':l})
def editprofile(request):
    if(request.method=='POST'):
        pimage=request.FILES.get("pimage")
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        status=request.POST.get("status")
        city=request.POST.get("city")
        country=request.POST.get("country")
        user=request.user
        p=user.profile
        p.profile_image=pimage
        p.name=name
        p.phone=phone
        p.city=city
        p.status=status
        p.country=country
        p.save()
        return redirect("/userpage/result")
    else:
        return render(request,'editprofile.html')
def logout_user(request):
    return logout_view(request)
def linkprofile(request):
    username=request.POST.get("search")
    user=Post.objects.all()
    return render(request,"mypost.html",{'posts':user})