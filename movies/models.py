from django.db import models
from actors.admin import Actor

class Movie(models.Model):
    title = models.CharField(max_length=100)
    actor = models.ManyToManyField(Actor, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Film(Movie):
    length = models.CharField(max_length=100)

    def __str__(self):
        return self.length

class Commercial(Movie):
    company = models.CharField(max_length=200)

    def __str__(self):
        return self.title
        
