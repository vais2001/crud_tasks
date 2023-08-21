from django.db import models

# Create your models here.
class Worker(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    phone_number=models.CharField(max_length=255)
    address=models.CharField(max_length=300,null=True,blank=True)
    worker_id=models.IntegerField(primary_key=True,null=False)
