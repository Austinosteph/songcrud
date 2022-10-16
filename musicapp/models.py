from django.db import models
from datetime import datetime


# Create your models here.
class artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

class song(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(default=datetime.today)
    released = models.DateField()
    likes = models.BooleanField(default=True)
    artiste_id = models.CharField(max_length=15)

class lyric(models.Model):
    content = models.CharField(max_length=100)
    song_id = models.CharField(max_length=15)
