from django.contrib import admin
from .models import Movie, Actor, Comment

admin.site.register([Movie, Actor, Comment])

