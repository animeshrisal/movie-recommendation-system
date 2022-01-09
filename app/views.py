from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from app.forms import MovieForm
from .models import Movie

# Create your views here.
def home_page(request):
    return render(request, 'home.html')
    # return HttpResponse("Welcome to django class")

def about_page(request):
    return render(request, 'about.html')

def get_movies(request):
    movies = Movie.objects.all()
    return render(request, 'movies.html', {'movies': movies})

def get_movie_details(request, id):
    movie = Movie.objects.get(id=id)
    context = { 
        'is_favorite': False
    }

    if movie.favorite.filter(pk=request.user.pk).exists():
        context['is_favorite'] = True
    
    return render(request, 'movie_description.html', {'movie': movie, 'context': context})

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
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return redirect('/movie/')


    return render(request, 'signup.html', {'form': form})

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
    movies =request.user.favorite.all()
    return render(request, 'user_favorite.html', {'movies': movies})

