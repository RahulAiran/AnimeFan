from django.db import models

# Create your models here.

class Anime(models.Model):
    anime_id = models.IntegerField(null=True)
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    animetype = models.CharField(max_length=100)
    episodes = models.IntegerField(null=True)
    rating = models.FloatField(null=True)
    members = models.IntegerField(null=True)
    mood = models.CharField(max_length=15)

    def __str__(self):
        return self.name