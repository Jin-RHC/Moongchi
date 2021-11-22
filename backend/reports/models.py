from django.db import models
from django.conf import settings
# from community.models import Review, Comment, NestedComment, Rating

# Create your models here.
class ReviewReport(models.Model):
    content = models.CharField(max_length=200)
    review_pk = models.ForeignKey('community.Review', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='review_reports')
    created_at = models.DateTimeField(auto_now_add=True)


class CommentReport(models.Model):
    content = models.CharField(max_length=200)
    comment = models.ForeignKey('community.Comment' ,on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='comment_reports')
    created_at = models.DateTimeField(auto_now_add=True)


class NestedCommentReport(models.Model):
    content = models.CharField(max_length=200)
    nested_comment = models.ForeignKey('community.NestedComment', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='nested_comment_reports')
    created_at = models.DateTimeField(auto_now_add=True)


class RatingReport(models.Model):
    content = models.CharField(max_length=200)
    rating = models.ForeignKey('community.Rating', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='rating_reports')
    created_at = models.DateTimeField(auto_now_add=True)