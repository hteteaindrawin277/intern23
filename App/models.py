from django.db import models

class Info(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phnumber = models.CharField(max_length=15)
    degree = models.CharField(max_length=20)

# Create your models here.
