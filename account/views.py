from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from student.models import profile
from django.core.files.storage import FileSystemStorage
from leads.models import NewLead
from university.models import university
from .models import formaddmision
# Create your views here.


def login_attempt(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        user = User.objects.filter(username=username).first()
        
        if user is None:
            context = {'message' : 'No user found' , 'class' : 'danger'}
            return render(request,'login.html' , context)
        else:
            user = authenticate(username = username , password = password)
            if user is None:
                context = {'message' : 'Invalid credentials' , 'class' : 'danger'}
                return render(request,'login.html' , context)
            else:
                login(request , user)
                return redirect('home')            
    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_email = request.POST.get('email')
        phone = request.POST.get('phoneno')
        leads = NewLead.objects.create(leadname=username , phone = phone)
        
        user = User.objects.filter(username=username)
        if user:
            context = {'message' : 'User already exists' , 'class' : 'danger'}
            return render(request,'register.html' , context)
        else :
            context = {'message' : 'User created successfully' , 'class' : 'success'}
            user = User.objects.create_user(username=username, email=user_email, password=password)
            user.save()
            user = authenticate(username = username , password = password)
            login(request , user)
            return redirect('home') 
        
    return render(request,'register.html')



def logout_attempt(request):
    request.session.profile = None
    logout(request)
    return redirect('/')

@login_required
def profilePage(request):
    profiles = profile.objects.filter(user = request.user)
    universities = university.objects.all().order_by("?")[0:3]
    context = {'profile':profiles,'universities':universities}
    print(profiles)
    if profiles:
        return render(request,'profile.html',context)
    else:
        return redirect('profileform')


# @login_required
# def applicationregistered(request):
#     application = formaddmision.objects.filter(user = request.user)
#     universities = university.objects.all().order_by("?")[0:3]
#     context = {'formregister':application,'universities':universities}
#     return render(request,'registerapplication.html')


@login_required
def profileform(request):
    profiles = profile.objects.filter(user = request.user)
    if profiles:
        return redirect('profilepage')
    else:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            address = request.POST.get('address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            pincode = request.POST.get('pincode')
            phono = request.POST.get('phono')
            date = request.POST.get('date')
            ReferalCode = request.POST.get('ReferalCode')
            # profile = request.FILES.get('profile')
            # Validate the data
            
            if first_name and last_name and address and city and state and pincode and phono and date:
                profile.objects.create(user=request.user,PhoneNo=phono, firstname=first_name, lastname=last_name , address=address, city=city , state=state, pincode=pincode, birth_date=date,referalcode=ReferalCode)
                return redirect('profilepage')
            
            
        return render(request,'profileform.html')


@login_required
def addmission(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        phono = request.POST.get('phono')
        college = request.POST.get('college')
        if first_name and last_name and  phono and college:
            formaddmision.objects.create(user=request.user,PhoneNo=phono, firstname=first_name, lastname=last_name , address=address,  college=college)
            return render(request,'registersucess.html')
    return render(request,'addmissionform.html')


