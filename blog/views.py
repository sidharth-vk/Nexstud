from django.shortcuts import render
from .models import blog,Newsletter
from django.core.paginator import Paginator
from django.contrib.auth.models import User
# Create your views here.
def bloglist(request):
    if request.method == "POST":
        username = request.user
        email = request.POST.get('email')
        Newsletter.objects.create(user=username,email=email)
    blogs = blog.objects.all()
    allblogs = blog.objects.all().order_by("?")[0:4]
    paginator = Paginator(blogs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'blog':page_obj,'allblogs':allblogs}
    return render(request,'blog.html',context)


def singleblog(request,pk):
    if request.method == "POST":
        username = request.user
        email = request.POST.get('email')
        Newsletter.objects.create(user=username,email=email)
    blogs = blog.objects.filter(slug=pk)
    allblogs = blog.objects.all().order_by("?")[0:4]
    context = {'blog':blogs,'allblogs':allblogs}
    return render(request,'single-blog.html',context)