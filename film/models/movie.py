from django.db import models


class Movie(models.Model):
    actors = models.ManyToManyField('Actor')
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    imdb = models.IntegerField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.name
