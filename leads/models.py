from django.db import models

# Create your models hm
class NewLead(models.Model):
    leadname = models.CharField(('Name'), max_length=250)
    phone = models.CharField(('Phone'), max_length=250)

    def __str__(self):
        return self.leadname