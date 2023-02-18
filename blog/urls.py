from django.urls import path
from . import views


urlpatterns = [
    path('',views.bloglist,name='blog'),
    path('<pk>',views.singleblog,name="blogdetail")
] 
