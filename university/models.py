from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
category = [
        ('ALL', 'ALL'),
        ('ENGINEERING', 'ENGINEERING'),
        ('MANAGEMENT', 'MANAGEMENT'),
        ('AGRICULTURE', 'AGRICULTURE'),
        ('ALLIED', 'ALLIED'),
        ('MBBS', 'MBBS'),
        ('PARAMEDICAL', 'PARAMEDICAL'),
        ('NURSING', 'NURSING')
    ]

class Course(models.Model):
    name = models.CharField(('Course'),max_length=100)

    def __str__(self):
        return self.name




class university(models.Model):
    college_name = models.CharField(("College Name"), max_length=100)
    university_name = models.CharField(("University Name"), max_length=100)
    University_category = models.CharField(('Category'),choices = category, max_length=250)
    university_courses = models.CharField(('Course'), max_length=250)
    university_img = models.ImageField(("Image"), upload_to="media/university_Image", height_field=None, width_field=None, max_length=None)
    university_state = models.CharField(("State"), max_length=100)
    university_city = models.CharField(("City"), max_length=100)
    university_map_location = models.CharField(("University Map Location Address"),max_length=10000)
    university_rating = models.CharField(("Rating"), max_length=100)
    university_Discription = RichTextField()
    search_keyword = RichTextField(blank=True, null=True)
    university_courses_tag = models.ManyToManyField(Course)
    university_top_list = models.BooleanField(("If the college is TopRated"),null=True, blank=True)
    slug = models.SlugField(max_length=1000, unique=True, blank=True, null=True)
    
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.college_name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.university_name

