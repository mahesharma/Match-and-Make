from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from userprofiles.models import Profile 
# Create your views here.
def home(request):
    return render(request,'index.html')
def signup(request):
    if request.method=='POST':
        username=request.POST.get('usernamesignup')
        email=request.POST.get('emailsignup')
        password=request.POST.get('passwordsignup')
        repass=request.POST.get('passwordsignup_confirm')
        user=User.objects.create_user(username=username,password=password,email=email)
        user.save()
        p=Profile(user=user)
        p.save()
        return redirect('/')
    else:
        return render(request,'signup.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/userpage/result')
        else:
            messages.info(request,'!!! invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect("/")