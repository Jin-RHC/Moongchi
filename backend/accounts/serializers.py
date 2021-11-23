from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from reports.serializers import (ReviewReportSerializer, CommentReportSerializer, NestedCommentReportSerializer,
    RatingReportSerializer)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'nickname', 'password',)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['nickname'] = user.nickname

        return token


class UserReportListSerializer(serializers.ModelSerializer):
    
    review_reports = ReviewReportSerializer(many=True)
    comment_reports = CommentReportSerializer(many=True)
    nested_comment_reports = NestedCommentReportSerializer(many=True)
    rating_reports = RatingReportSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('review_reports', 'comment_reports', 'nested_comment_reports',
            'rating_reports')
