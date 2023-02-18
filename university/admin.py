from django.contrib import admin
from django.utils.html import strip_tags
from .models import university, Course
from django.utils.safestring import mark_safe

# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('college_name','university_name', 'university_city','university_state')
    

admin.site.register(university,MyModelAdmin)

admin.site.register(Course)