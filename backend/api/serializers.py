from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Movie, Rating

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'no_of_ratings', 'avg_rating')

class MovieMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'movie')
