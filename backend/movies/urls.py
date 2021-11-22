from . import views

app_name = 'movies'

from django.urls import path, include

urlpatterns = [
    path('movielist/', views.movie_list, name='movie_list'),
    # path('initializemovies/', views.initialize_movies, name='initialize_movies'),
    # path('initializegenres/', views.initialize_genres, name='initialize_genres'),
    # path('testmovie/', views.test_movie, name='test_movie'),
    
]