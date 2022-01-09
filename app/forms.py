from django.forms import ModelForm
from .models import Movie

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'homepage', 'description', 'release_date', 'runtime']