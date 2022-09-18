from django.db import models
#from django.contrib.auth.models import User


class Inventoryoff(models.Model):
    name = models.CharField(max_length=200)
    designation=models.CharField(max_length=50)
    grade=models.CharField(max_length=5)
    mobile= models.CharField(max_length=15)
    
 
        