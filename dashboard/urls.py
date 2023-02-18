
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name="dashhome"),
    path('student', views.Student,name="dashstudent"),
    path('student/pending', views.studentpending,name="studentpending"),
    path('student/completed', views.studentcompleted,name="studentcompleted"),
    path('newsletter', views.newsletter,name="dashnewsletter"),
     path('student/completed/<int:pk>/', views.Studentaddmcompletedbox, name='addmissioncompleted'),
    path('university', views.universityview,name="universitydash"),
    path('university/course', views.dashuniversitycourse,name="dashuniversitycourse"),
    # path('university/add', views.universityadd,name="universityadd"),
    path('lead/delete/<pk>', views.deletelead,name="deletelead"),
    path('university/delete/<pk>', views.deleteunivesity,name="deleteunivesity"),
] 
