from django.shortcuts import render,redirect
from leads.models import NewLead
from student.models import profile
from university.models import university
from blog.models import Newsletter
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, Group
# Create your views here.

agentc = ['admin','agent']

def home(request):
    user = User.objects.get(username=request.user)
    group = Group.objects.get(name='admin')
    if group in user.groups.all():
        leadname = NewLead.objects.all()
        context = {'lead':leadname}
        return render(request,'dashboardtemplate/dashboard.html',context)
    else :
        return redirect('home')


def Student(request):
    user = User.objects.get(username=request.user)
    group = Group.objects.get(name='admin')
    if group in user.groups.all():
        student = profile.objects.all()
        context = {'student':student}
        return render(request,'dashboardtemplate/dashstudent.html',context)
    else :
        return redirect('home')

def Studentaddmcompletedbox(request, pk):
    instance = profile.objects.get(pk=pk)
    instance.action = not instance.action
    instance.save()
    return redirect('dashstudent')



def deletelead(request, pk):
    user = User.objects.get(username=request.user)
    group = Group.objects.get(name='admin')
    if group in user.groups.all():
        leadname = NewLead.objects.get(id=pk)
        leadname.delete()
        return redirect('dashhome')
    else :
        return redirect('home')


def newsletter(request):
    user = User.objects.get(username=request.user)
    group = Group.objects.get(name='admin')
    if group in user.groups.all():
        news = Newsletter.objects.all()
        context = {'news':news}
        return render(request,'dashboardtemplate/dashnewsletter.html',context)
    else :
        return redirect('home')

def universityview(request):
    user = User.objects.get(username=request.user)
    group = Group.objects.get(name='admin')
    if group in user.groups.all():
        universities = university.objects.all()
        context = {'university':universities}
        return render(request,'dashboardtemplate/dashuniversity.html',context)
    else :
        return redirect('home')

def deleteunivesity(request, pk):
    user = User.objects.get(username=request.user)
    group = Group.objects.get(name='admin')
    if group in user.groups.all():
        universities = university.objects.get(id=pk)
        universities.delete()
        return redirect('universitydash')
    else :
        return redirect('home')

def dashuniversitycourse(request):
    user = User.objects.get(username=request.user)
    group = Group.objects.get(name='admin')
    if group in user.groups.all():
        ENGINEERING = university.objects.filter(University_category='ENGINEERING')
        MANAGEMENT = university.objects.filter(University_category='MANAGEMENT')
        AGRICULTURE = university.objects.filter(University_category='AGRICULTURE')
        ALLIED = university.objects.filter(University_category='ALLIED')
        MBBS = university.objects.filter(University_category='MBBS')
        PARAMEDICAL = university.objects.filter(University_category='PARAMEDICAL')
        NURSING = university.objects.filter(University_category='NURSING')
        context = {'ENGINEERING':ENGINEERING,"MANAGEMENT":MANAGEMENT,"AGRICULTURE":AGRICULTURE,"ALLIED":ALLIED,"MBBS":MBBS,"PARAMEDICAL":PARAMEDICAL,'NURSING':NURSING}
        return render(request,'dashboardtemplate/dashuniversitycourse.html',context)
    else :
        return redirect('home')


# def universityadd(request):
#     user = User.objects.get(username=request.user)
#     group = Group.objects.get(name='admin')
#     if group in user.groups.all():
#         if request.method == 'POST' and request.FILES['myfile']:
#             myfile = request.FILES['myfile'] 
#             fs= FileSystemStorage()
#             filename = fs.save(myfile.name, myfile)
#             url = fs.url(filename)
#             collegename = request.POST.get('collegename')
#             universityname = request.POST.get('universityname')
#             category = request.POST.get('category')
#             location = request.POST.get('location')
#             Discription = request.POST.get('Discription')
#             course = request.POST.get('course')
#             city = request.POST.get('city')
#             state = request.POST.get('state')
#             rating = request.POST.get('rating')
#             if collegename and universityname and category and location and Discription and course and city and state and rating :
#                 university.objects.create(college_name=collegename, university_name=universityname, University_category=category,  university_state=state, university_city=city , university_map_location=location, university_rating=rating, university_Discription=Discription, university_img=url)
#         return render(request,'dashboardtemplate/dashuniversityadd.html')

#     else :
#         return redirect('home')


def studentpending(request):
    user = User.objects.get(username=request.user)
    group = Group.objects.get(name='admin')
    if group in user.groups.all():
        student = profile.objects.filter(action=False)
        context = {'student':student}
        return render(request,'dashboardtemplate/studentpending.html',context)
    else :
        return redirect('home')

def studentcompleted(request):
    user = User.objects.get(username=request.user)
    group = Group.objects.get(name='admin')
    if group in user.groups.all():
        student = profile.objects.filter(action=True)
        context = {'student':student}
        return render(request,'dashboardtemplate/studentcompleted.html',context)
    else :
        return redirect('home')
    