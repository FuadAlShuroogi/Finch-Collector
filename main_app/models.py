from django.db import models
from django.contrib import admin

class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    age = models.IntegerField()

def __str__(self):
    return self.name

admin.site.register(Finch)

