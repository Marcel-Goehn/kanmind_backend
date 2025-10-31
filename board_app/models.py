from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=255)
    member = models.ManyToManyField(User, blank=True)
    owner = models.OneToOneField(User)
    
    
class Task(models.Model):
    pass