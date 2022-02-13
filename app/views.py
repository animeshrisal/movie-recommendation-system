from datetime import datetime
from operator import ge
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from app.forms import MovieForm, ReviewForm, UploadForm
from app.ml import get_recommendation_for_movie
from rest_framework import viewsets

from app.serializers import MovieSerializer
from .models import Movie, Review
import pandas as pd
from django.db import transaction

from rest_framework import generics

# Create your views here.


def home_page(request):
    return render(request, 'home.html')
    # return HttpResponse("Welcome to django class")


def about_page(request):
    return render(request, 'about.html')


def get_movies(request, page_number):
    if page_number < 1:
        page_number = 1

    pagination = {
        'previous_page': page_number - 1,
        'current_page': page_number,
        'next_page': page_number + 1
    }

    page_size = 10
    movies = Movie.objects.all()[(page_number-1)
                                 * page_size:page_number*page_size]
    return render(request, 'movies.html', {'movies': movies, 'pagination': pagination})


def update_movie(request, id):
    movie = Movie.objects.get(pk=id)

    if request.method == "POST":
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('/movie/{}'.format(id))
    elif request.method == "GET":
        movie_form = MovieForm(instance=movie)
    return render(request, 'update_movie.html', {'form': movie_form})


def get_movie_details(request, id):
    review_form = ReviewForm()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.movie_id = id
            review.user_id = request.user.id
            review.save()

    movie = Movie.objects.get(id=id)
    reviews = Review.objects.filter(movie=movie).order_by('-created_at')[0:4]
    context = {
        'is_favorite': False
    }

    if movie.favorite.filter(pk=request.user.pk).exists():
        context['is_favorite'] = True

    movie_ids = get_recommendation_for_movie(id)

    recommended_movies = Movie.objects.filter(id__in=movie_ids)

    return render(request, 'movie_description.html',
                  {'movie': movie,
                   'context': context,
                   'reviews': reviews,
                   'review_form': review_form,
                   'recommended_movies': recommended_movies
                   })


def post_movie(request):
    form = MovieForm()

    if request.method == "POST":
        movie_form = MovieForm(request.POST)

        if movie_form.is_valid():
            movie_form.save()

            return redirect('/movie/')

    return render(request, 'post_movie.html', {'form': form})


def signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return redirect('/movie/')

    return render(request, 'signup.html', {'form': form})


def signin(request):
    form = AuthenticationForm()
    if request.method == "POST":
        print(request.POST)
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return redirect('/movie/')

    return render(request, 'signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('/movie/')


def add_to_favorite(request, id):
    movie = Movie.objects.get(id=id)
    movie.favorite.add(request.user)

    return redirect('/movie/{0}'.format(id))


def remove_from_favorites(request, id):
    movie = Movie.objects.get(id=id)
    movie.favorite.remove(request.user)

    return redirect('/movie/{0}'.format(id))


def get_user_favorites(request):
    movies = request.user.favorite.all()
    return render(request, 'user_favorite.html', {'movies': movies})


def upload_dataset(request):
    file_form = UploadForm()
    error_messages = {}

    if request.method == "POST":
        file_form = UploadForm(request.POST, request.FILES)
        try:
            if file_form.is_valid():
                dataset = pd.read_csv(request.FILES['file'])
                new_movies_list = []
                dataset['budget'] = dataset['budget'].fillna(0)
                with transaction.atomic():
                    for index, row in dataset.iterrows():
                        movie = Movie(
                            title=row['title'],
                            budget=row['budget'],
                            genres=row['genres'],
                            keywords=row['keywords'],
                            overview=row['overview'],
                            tagline=row['tagline'],
                            cast=row['cast'],
                            director=row['director']
                        )

                        new_movies_list.append(movie)

                Movie.objects.bulk_create(new_movies_list)
        except Exception as e:
            error_messages['error'] = e

    return render(request, 'upload_dataset.html', {'form': file_form, 'error_messages': error_messages})


class RetrieveMovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
