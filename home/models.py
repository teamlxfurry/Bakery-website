from datetime import date
import email
from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=100)
    phone= models.CharField(max_length=14)
    email= models.CharField(max_length=100)
    feedback =models.TextField()
    

    def __str__(self) :
        return self.name