
from django.urls import path, include
from . import views

handler404 = views.handler404

urlpatterns = [
    path('', views.homepage,name="home"),
    path('talk-to-expert', views.talktous,name="talktous"),
] 
