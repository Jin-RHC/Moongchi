from . import views
from django.urls import path, include

app_name = 'community'

urlpatterns = [
    # 영화 전체 리뷰
    path('review/', views.review_lists, name='review_lists'),

    # 영화 좋아요, 싫어요
    path('<int:movie_id>/like/', views.movie_like, name='movie_like'),
    path('<int:movie_id>/dlike/', views.movie_dlike, name='movie_dlike'),

    # 해당 영화의 리뷰리스트, 작성
    path('<int:movie_id>/review/', views.review_list_create, name='review_list_create'),

    # 리뷰 수정, 삭제, 좋아요, 싫어요
    path('<int:movie_id>/review/<int:review_id>/', views.review_update_delete, name='review_update_delete'),
    path('<int:movie_id>/review/<int:review_id>/like/', views.review_like, name='review_like'),
    path('<int:movie_id>/review/<int:review_id>/dlike/', views.review_dlike, name='review_dlike'),

    # 댓글 작성, 삭제, 좋아요, 싫어요
    path('<int:review_id>/comment/', views.comment_create, name='comment_create'),
    path('<int:review_id>/comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('<int:review_id>/comment/<int:comment_id>/like/', views.comment_like, name='comment_like'),
    path('<int:review_id>/comment/<int:comment_id>/dlike/', views.comment_dlike, name='comment_dlike'),

    # 대댓글 작성, 삭제, 좋아요, 싫어요
    path('<int:comment_id>/nestedcomment/', views.nestedcomment_create, name='nestedcomment_create'),
    path('<int:comment_id>/nestedcomment/<int:nestedcomment_id>/', views.nestedcomment_delete, name='nestedcomment_delete'),
    path('<int:comment_id>/nestedcomment/<int:nestedcomment_id>/like/', views.nestedcomment_like, name='nestedcomment_like'),
    path('<int:comment_id>/nestedcomment/<int:nestedcomment_id>/dlike/', views.nestedcomment_dlike, name='nestedcomment_dlike'),
    
    # 별점 작성
    path('<int:movie_id>/rating/', views.rating_list_create, name='rating_list_create'),
    # 별점 삭제, 좋아요, 싫어요
    path('<int:movie_id>/rating/<int:rating_id>/', views.rating_delete, name='rating_delete'),
    path('<int:movie_id>/rating/<int:rating_id>/like/', views.rating_like, name='rating_like'),
    path('<int:movie_id>/rating/<int:rating_id>/dlike/', views.rating_dlike, name='rating_dlike'),
]