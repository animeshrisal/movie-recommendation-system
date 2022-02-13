from unittest.util import _MAX_LENGTH
from rest_framework import serializers

from app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    budget = serializers.IntegerField()
    genres = serializers.CharField()
    keywords = serializers.CharField()
    overview = serializers.CharField()
    tagline = serializers.CharField()
    cast = serializers.CharField()
    director = serializers.CharField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'budget', 'genres', 'keywords',
                  'overview', 'tagline', 'cast', 'director')
