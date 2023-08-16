from django.db import models

# Create your models here.
class Worker(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    phone_number=models.CharField(max_length=255)



class Unit(models.Model):
    worker=models.ForeignKey(Worker,on_delete=models.CASCADE,null=True)
    
    
class Visit(models.Model):
    date_time=models.DateTimeField(auto_now=True,null=True,blank=True)
    unit=models.ForeignKey(Unit,on_delete=models.CASCADE)
    latitude=models.FloatField(null=True,blank=True)
    longitude =models.FloatField(null=True,blank=True)