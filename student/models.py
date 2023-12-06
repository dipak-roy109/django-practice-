from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    department = models.CharField(max_length=50)
    phone = models.CharField(max_length=16)
