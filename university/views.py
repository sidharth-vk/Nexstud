from django.shortcuts import render, redirect
from .models import university 
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

def UniversityView(request):
    universityview = university.objects.all().order_by("?")
    paginator = Paginator(universityview, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'university': page_obj}
    return render(request, 'search.html',context)



@login_required
def University(request,pk):
    universityview = university.objects.filter(slug = pk)
    category = universityview[0].University_category
    alluniversity = university.objects.filter(University_category=category).order_by("?")[0:3]
    # otheruniversity = university.objects.filter(University_category=universityview.University_category)
    context = {'university': universityview, 'alluniversity':alluniversity}
    return render(request,'university.html',context)



def UniversityViewSearch(request):
    query = request.GET['query']
    UniversitySearch = university.objects.filter(Q(college_name__icontains = query) | Q(university_city__icontains = query) | Q(University_category__icontains = query) | Q(search_keyword__icontains = query) )
    paginator = Paginator(UniversitySearch, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'university': page_obj,'query':query}
    return render(request, 'search_filter.html',context)
