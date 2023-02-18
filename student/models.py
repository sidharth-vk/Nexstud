from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(("First Name"), max_length=250, blank=True,null=True)
    lastname = models.CharField(("Last Name"), max_length=250, blank=True,null=True)
    # userid = models.CharField(("User ID"), unique=True, max_length=50, blank=True,null=True)
    PhoneNo = models.PositiveIntegerField(('Phone No'),blank=True,null=True)
    bio = models.TextField(max_length=500, blank=True,null=True)
    address = models.CharField(('Address'),max_length=250,blank=True,null=True)
    city = models.CharField(('City'),max_length=250,blank=True,null=True)
    state = models.CharField(('State'),max_length=250,blank=True,null=True)
    pincode = models.PositiveIntegerField(('Pincode'),blank=True,null=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True,null=True)
    action = models.BooleanField(('Admission done: '),default=False)
    verify = models.BooleanField(('Verified account: '),default=False)
    referalcode = models.CharField(("Referal Code"), max_length=250, blank=True,null=True)
    
    def __str__(self):
        return self.user.username
