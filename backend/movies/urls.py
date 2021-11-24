from . import views
from django.urls import path, include

app_name = 'movies'

urlpatterns = [
    # 메인에 뜰 추천 영화 리스트 반환(현재 상영작, 평점순, 인기순(요새 평점이 많이 달린 순으로))
    # {"now-playing": 현재 상영작 리스트, "high-rates": 평점순 리스트,
    # "popular": 인기순 리스트} 식으로 응답이 올 겁니다!!
    path('mainmovies/', views.mainmovies, name='mainmovies'),


    # 고객별 맞춤 추천리스트
    path('recommended/', views.recommended_movie_list, name='recommended_movie_list'),


    # 영화 리스트(그냥 전부 다) 조회
    path('movielist/<int:page>/', views.movie_list, name='movie_list'),

    # 영화 상세 조회
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),

    # 영화 검색
    path('moviesearch/<str:title>/', views.movie_search, name='movie_search'),





    # get 요청으로 딱 한 번 실행하면 되는!!! rating_average 추가 코드(실행 후 다시 각주 처리 바랍니다...)
    # path('making-rating-average/', views.making_rating_average, name='making_rating_average')
    # path('initializemovies/', views.initialize_movies, name='initialize_movies'),
    # path('initializegenres/', views.initialize_genres, name='initialize_genres'),
    # path('testmovie/', views.test_movie, name='test_movie'),
    
]