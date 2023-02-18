from django.contrib import admin
from .models import blog,Newsletter
# Register your models here.
admin.site.register(blog)


class MyModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'email')

admin.site.register(Newsletter,MyModelAdmin)
    