from django.db import models
from datetime import datetime


# Create your models here.
class artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return self.first_name
    

class song(models.Model):
    artiste_id = models.ForeignKey(artiste, on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    date = models.DateField(default=datetime.today)
    released = models.DateField(default=datetime.today)
    likes = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class lyric(models.Model):
    song_id = models.ForeignKey(song, on_delete = models.CASCADE)
    content = models.CharField(max_length=100)
    
    def __str__(self):
        return self.song_id
