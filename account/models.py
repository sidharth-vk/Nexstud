from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class formaddmision(models.Model):
    user = models.CharField(("user"), max_length=250, blank=True,null=True)
    firstname = models.CharField(("First Name"), max_length=250, blank=True,null=True)
    lastname = models.CharField(("Last Name"), max_length=250, blank=True,null=True)
    PhoneNo = models.PositiveIntegerField(('Phone No'),blank=True,null=True)
    address = models.CharField(('Address'),max_length=1250,blank=True,null=True)
    college = models.CharField(('Required College'),max_length=1250,blank=True,null=True)
    def __str__(self):
        return self.user