from django.urls import path
from . import views
urlpatterns = [
    path('post',views.post,name='post'),
    path('result',views.result,name='result'),
    path('mypost',views.mypost,name='mypost'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('logout_user',views.logout_user,name='logout_user'),
    path('linkprofile',views.linkprofile,name='linkprofile'),
]




































