from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="Home Page"),
    path('about/', views.about_page, name="About Page"),
    path('movie/', views.get_movies, name="Movie Page"),
    path('movie/<int:id>', views.get_movie_details, name="Movie Page"),
    path('post_movie/', views.post_movie, name="Post Movie"),
    path('signup/', views.signup, name="User Sign Up"),
    path('signout/', views.signout, name="User Sign Out"),
    path('add_to_favorite/<int:id>', views.add_to_favorite, name="Add to favorite"),
    path('remove_from_favorites/<int:id>', views.remove_from_favorites, name="Remove from favorite"),
    path('user_favorites', views.get_user_favorites, name="Get User Favorites")
]