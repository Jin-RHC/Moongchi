from django.shortcuts import render
from .models import Movie, Genre, Director, Actor
from community.models import Rating
from pprint import pprint
from accounts.models import User
import requests
from justwatch import JustWatch
from moongchi.my_settings import MY_SECRET
import pickle


A_K = MY_SECRET['TMDB_KEY']

NATION_CODE = {'KR': '대한민국', 'JP': '일본', 'US': '미국', 'GB': '영국', 'FR': '프랑스', 
    'HK': '홍콩', 'CA': '캐나다', 'ID': '인도네시아', 'TH': '태국', 'IN': '인도', 'CN': '중국', 
    'TW': '대만', 'DE': '독일', 'ES':'스페인', 'RU': '러시아', 'NL': '네덜란드', 'NO' :'노르웨이',
    'DK': '덴마크', 'MX': '멕시코', 'NZ': '뉴질랜드', 'IT': '이탈리아', 'PT': '포르투갈',
    'BR': '브라질', 'AR': '아르헨티나', 'PE': '페루', 'CO': '콜롬비아'}

with open('movies/recommendations.p', 'rb') as file:
    recommendations = pickle.load(file)


# Create your views here.

#장르 받아오기. 초기 사용으로만!!!
def initialize_genres(request):
    initialize_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={A_K}&language=ko-KR'
    res = requests.get(initialize_url)
    data = res.json()
    for datum in data.get('genres'):
        genre = Genre()
        genre.id = datum.get('id')
        genre.name = datum.get('name')
        genre.save()
    
    pprint(Genre.objects.all())

# 영화 데이터 받아오기. 초기 사용으로만!!!
def initialize_movies(request):

    # for page in range(1, 501):
    #     list_url = f'https://api.themoviedb.org/3/movie/popular?api_key={A_K}&language=ko-KR&page={page}'
    #     res = requests.get(list_url).json().get('results')
    #     pprint(res)
    #     print(type(res))
    def isenko(word): # 영화 필터링을 위해 주어진 문자가 영어 혹은 한글이어야만 저장
        for ch in word[:min([3, len(word)])]:
            JAMO_START_LETTER = 44032
            JAMO_END_LETTER = 55203
            if not((JAMO_START_LETTER <= ord(ch) <= JAMO_END_LETTER) or (ord(ch) <= 125)):
                return False
            return True


    def is_netflix(query):
        just_watch = JustWatch(country='KR')
        result = just_watch.search_for_item(query=query).get('items')
        if result:
            target = result[0]
            if target.get('title') == query and target.get('offers'):
                for item in target.get('offers'):
                    if item.get('package_short_name') == 'nfx':
                        return True
        return False


    for page in range(231, 501):
        print(page, end=', ')
        list_url = f'https://api.themoviedb.org/3/movie/popular?api_key={A_K}&language=ko-KR&page={page}'
        res = requests.get(list_url).json()
        results = res.get('results')
        for result in results:
            # 정보가 불충분한 영화는 제외
            if not (result.get('poster_path', '') and result.get('overview', '')):
                continue
            if not isenko(result.get('title')):
                continue

            movie_id = result.get('id')
            detail_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={A_K}&language=ko-KR&append_to_response=videos,credits'
            data = requests.get(detail_url).json() # 디테일 조회
            
            # 저장하기 위한 객체 생성 및 단순 속성 추가
            movie = Movie()
            director = Director()
            movie.id = movie_id
            movie.title = data.get('title')
            movie.overview = data.get('overview')
            movie.poster_path = data.get('poster_path', '')
            movie.popularity = data.get('popularity')
            movie.is_netflix = is_netflix(data.get('title'))
            if data.get('release_date', ''):
                movie.release_date = data.get('release_date')

            # 국가 추가
            if data.get('original_language', '') == 'ko':
                movie.country = '대한민국'
            elif data.get('original_language', '') == 'en':
                for country in data.get('production_countries', ''):
                    if country.get('iso_3166_1') == 'US':
                        movie.country = '미국'
            elif data.get('production_countries', ''):
                movie.country = NATION_CODE.get(data.get('production_countries')[0].get('iso_3166_1'), data.get('production_countries')[0].get('iso_3166_1'))       

            # 비디오 주소 추가
            for video in data.get('videos').get('results'):
                if video.get('type') == 'Trailer':
                    movie.video_path = video.get('key')
                    break
            
            movie.save()
            
            # 장르 추가
            for temp_genre in data.get('genres'):
                genre_id = temp_genre.get('id')
                genre = Genre.objects.get(pk=genre_id)
                movie.genres.add(genre)

            # 감독 추가
            for crew in data.get('credits').get('crew'):
                if crew.get('job') == 'Director':
                    try:
                        director = Director.objects.get(pk=crew.get('id'))
                        director.movies.add(movie)
                        break

                    except:
                        director = Director()
                        director.id = crew.get('id')
                        director.name = crew.get('original_name')
                        director.profile_path = crew.get('profile_path')
                        director.save()
                        director.movies.add(movie)
                        break
            
            # 배우 추가
            for cast in data.get('credits').get('cast')[:min([5, len(data.get('credits').get('cast'))])]:
                try:
                    actor = actor.objects.get(pk=cast.get('id'))
                    actor.movies.add(movie)

                except:
                    actor = Actor()
                    actor.id = cast.get('id')
                    actor.name = cast.get('original_name')
                    actor.profile_path = cast.get('profile_path')
                    actor.save()
                    actor.movies.add(movie)


            # 초기 데이터를 위해 별점 및 한줄평 추가
            rating = Rating()
            rating.movie = movie
            rating.user = User.objects.get(username='admin')            
            rating.rating = round(data.get('vote_average'))

            if data.get('vote_average') >= 8.3:
                rating.content = 'ㄹㅇ 명작입니다...'
            
            elif data.get('vote_average') >= 7:
                rating.content = '괜찮게 봤어요'

            elif data.get('vote_average') >= 6:
                rating.content = '그저 그래요'

            elif data.get('vote_average') >= 5:
                rating.content = '별로예요'

            else:
                rating.content = '안 본 눈 삽니다,,,'

            rating.save()

    print('done')
            
    
def test_movie(request):

    print(recommendations[809970])

    print(recommendations[809970][2])

    print(type(recommendations[809970][2]))

    # movies = Movie.objects.all()

    # count = 0
    # for movie in movies:

    #     if len(movie.overview) <= 50:
    #         print(movie.title, ':', movie.overview)
    #     #         movie.delete()
        
    #     if not movie.video_path:
    #         count += 1

    # print(count)


            






    # detail_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={A_K}&language=ko-KR&append_to_response=videos,credits'
