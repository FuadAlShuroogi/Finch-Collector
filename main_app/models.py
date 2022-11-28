from django.db import models
from django.contrib import admin
from django import forms  

class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    age = models.IntegerField()
    finch_image = models.ImageField(null=True, blank=True,upload_to='images/') 

def __str__(self):
    return self.name

admin.site.register(Finch)

