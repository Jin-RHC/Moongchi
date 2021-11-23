from django.db.models.aggregates import Avg
from rest_framework import serializers
from .models import Movie, Director, Actor
from community.models import Rating
from django.contrib.auth import get_user_model


class MovieListSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('title', 'id', 'poster_path', 'is_netflix', 'rate')

    def get_rate(self, instance):
        return instance.rating_set.aggregate(rate=Avg('rating'))


class MovieDetailSerializer(serializers.ModelSerializer):

    class DirectorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Director
            fields = ('name', 'profile_path')

    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name', 'profile_path')

    class RatingSerializer(serializers.ModelSerializer):
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('id', 'username', 'nickname')
        
        user = UserSerializer(read_only=True)

        class Meta:
            model = Rating
            exclude = ('reported_users', 'like_users', 'dlike_users', 'movie')

    
    directors = DirectorSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    rate = serializers.SerializerMethodField()
    rating_set = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, instance):
        return instance.rating_set.aggregate(rate=Avg('rating'))

class MovieSearchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title',  'poster_path')














# class MovieListSerializer(serializers.ModelSerializer):

#     class DirectorSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Director
#             fields = ('name', 'profile_path')

#     class ActorSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Actor
#             fields = ('name', 'profile_path')
    
#     directors = DirectorSerializer(many=True, read_only=True)
#     actors = ActorSerializer(many=True, read_only=True)
#     rate = serializers.SerializerMethodField()

#     class Meta:
#         model = Movie
#         fields = '__all__'

#     def get_rate(self, instance):
#         return instance.rating_set.aggregate(rate=Avg('rating'))




# class MovieListSerializer(serializers.ModelSerializer):

#     rate = serializers.SerializerMethodField()

#     rate_avg = serializers.FloatField(
#         source='rating_set__rating.Avg',
#         read_only=True
#     )

#     class Meta:
#         model = Movie
#         fields = ('title', 'id', 'poster_path', 'is_netflix', 'rate', 'rate_avg')

#     def get_rate(self, instance):
#         return instance.rating_set.aggregate(rate=Avg('rating'))