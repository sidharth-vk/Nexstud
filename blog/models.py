from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class blog(models.Model):
    title = models.CharField(("Short Title"), max_length=50)
    longtitle = models.CharField(("Long Title"), max_length=150)
    BlogContent = RichTextField()
    quote = models.CharField(("Quote"), max_length=250)
    author = models.CharField(("Author"), max_length=150)
    keywords = models.CharField(("Keywords"), max_length=150)
    image = models.ImageField(("Image"), upload_to='blogimage')
    date = models.PositiveIntegerField(('Date'),blank=True,null=True)
    month = models.CharField(('Month'),max_length=12)
    slug =  models.SlugField(max_length=1000, unique=True, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Newsletter(models.Model):
    user = models.CharField(('Name'),max_length=150)
    email = models.CharField(('Email'),max_length=150)
