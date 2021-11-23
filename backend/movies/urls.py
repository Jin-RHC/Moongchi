from . import views
from django.urls import path, include

app_name = 'movies'

urlpatterns = [
    # 영화 리스트 조회
    path('movielist/<int:page>/', views.movie_list, name='movie_list'),

    # 영화 상세 조회
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),

    # 영화 검색
    path('moviesearch/<str:title>/', views.movie_search, name='movie_search'),

    
    # path('initializemovies/', views.initialize_movies, name='initialize_movies'),
    # path('initializegenres/', views.initialize_genres, name='initialize_genres'),
    # path('testmovie/', views.test_movie, name='test_movie'),
    
]