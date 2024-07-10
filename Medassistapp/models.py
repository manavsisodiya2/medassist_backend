from django.db import models

# Create your models here.
from django.db import models


class Doctors(models.Model):
    
    doctorname = models.CharField(max_length=100, blank=False, default='')
     
    gender = models.CharField(max_length=10, blank=False, default='')
    dob = models.CharField(max_length=25, blank=False, default='')
    address = models.CharField(max_length=150, blank=False, default='')
    emailid = models.CharField(max_length=100, blank=False, default='')
    mobileno = models.CharField(max_length=100, blank=False, default='')
    qualification = models.CharField(max_length=100, blank=False, default='')
    password = models.CharField(max_length=100, blank=False, default='')
    photograph = models.ImageField(upload_to='static/')

