from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.UniversityView,name="university"),
    path('nexel/<pk>', views.University,name="university_view"),
    path('search', views.UniversityViewSearch,name="search"),
] 
