from django.urls import path
from .views import (
    ListCommentApiView,
    PostApiView,
    ListPostApiView,
    CommentApiView,
    UpvoteApiView,
)

app_name = "news_board"
urlpatterns = [
    path("posts/", ListPostApiView.as_view()),
    path("posts/<int:post_id>/", PostApiView.as_view()),
    path("posts/<int:post_id>/comments/", ListCommentApiView.as_view()),
    path("posts/<int:post_id>/upvote/", UpvoteApiView.as_view()),
    path("comments/<int:comment_id>/", CommentApiView.as_view()),
]
