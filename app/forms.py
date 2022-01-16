from django import forms
from .models import Movie, Review

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'budget', 'genres',
            'keywords', 'overview', 'release_date',
            'tagline', 'cast', 'director'
        ]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review']

class UploadForm(forms.Form):
    file = forms.FileField()
