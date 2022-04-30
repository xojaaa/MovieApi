from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Movie, Actor, Comment
import datetime


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

    def validate_birthday(self, value):
        min_year = datetime.date(1950, 1, 1)
        if value.year < min_year.year:
            raise ValidationError(detail="value of year > 01/01/1950 ")
        return value


class MovieSerializer(serializers.ModelSerializer):
    # actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    movie_id = MovieSerializer()

    class Meta:
        model = Comment
        fields = "__all__"


