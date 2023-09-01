from django.db import models

# Create your models here.
from django.db import models
class Category(models.Model):
    categoryname = models.CharField(max_length=100, blank=False, default='')
    description= models.CharField(max_length=250,blank=False, default='')
    icon = models.CharField(max_length=200,blank=False, default='')
class States(models.Model):
    statename = models.CharField(max_length=100, blank=False, default='')
class City(models.Model):
    states = models.ForeignKey(
        States, on_delete=models.CASCADE)
    cityname = models.CharField(max_length=100, blank=False, default='')
class Doctors(models.Model):
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    doctorname = models.CharField(max_length=100, blank=False, default='')
     
    gender = models.CharField(max_length=10, blank=False, default='')
    dob = models.CharField(max_length=25, blank=False, default='')
    address = models.CharField(max_length=150, blank=False, default='')
    states = models.ForeignKey(States, on_delete=models.CASCADE,related_name="state")
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    emailid = models.CharField(max_length=100, blank=False, default='')
    mobileno = models.CharField(max_length=100, blank=False, default='')
    qualification = models.CharField(max_length=100, blank=False, default='')
    password = models.CharField(max_length=100, blank=False, default='')
    photograph = models.ImageField(upload_to='static/')

class Timings(models.Model):
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)   
    starttimings = models.CharField(max_length=100, blank=False, default='')
    endtimings = models.CharField(max_length=100, blank=False, default='')   
    days = models.CharField(max_length=200, blank=False, default='')
    status = models.CharField(max_length=45, blank=False, default='')
 