from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Message(models.Model):
    values = models.CharField(max_length=100000)
    username = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)
    room = models.CharField(max_length=1000)

    def __str__(self):
        return self.values

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)
    number = models.IntegerField()
    room = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.username