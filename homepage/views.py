from django.shortcuts import render
from blog.models import blog
# Create your views here.
def homepage(request):
    allblogs = blog.objects.all().order_by("?")[0:3]
    context = {'allblogs':allblogs}
    return render(request, 'index.html',context)


def handler404(request, exception):
    return render(request, '404.html', status=404)

def talktous(request):
    return render(request,'taltoexpert.html')