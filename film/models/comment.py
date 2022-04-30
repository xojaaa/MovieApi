from django.contrib.auth import get_user_model
from django.db import models

from film.models import Movie

User = get_user_model()


class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.CharField(max_length=2048)
    created_date = models.DateField()

