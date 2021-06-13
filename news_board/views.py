from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from news_board.models import Post, Comment
from news_board.permissions import IsAuthor
from news_board.serializers import PostSerializer, CommentSerializer


class ListPostApiView(APIView):
    """
    Class to get a list of news posts or create a new one.
    """
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request: Request) -> Response:
        post = request.data.get("post")
        serializer = self.serializer_class(data=post)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
        return Response(
            {"post": serializer.data}, status=status.HTTP_201_CREATED
        )

    def get(self, request: Request) -> Response:
        posts = Post.objects.all()
        serializer = self.serializer_class(posts, many=True)
        return Response({"posts": serializer.data}, status=status.HTTP_200_OK)


class PostApiView(APIView):
    """
    Class for CRUD operations to manage news posts.
    """
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly & IsAuthor]

    def get(self, request: Request, post_id: int) -> Response:
        post = get_object_or_404(Post, id=post_id)
        serializer = self.serializer_class(post)
        return Response({"post": serializer.data},
                        status=status.HTTP_200_OK)

    def patch(self, request: Request, post_id: int) -> Response:
        post = get_object_or_404(Post, id=post_id)
        self.check_object_permissions(request, post_id)
        update_data = request.data.get("post")
        serializer = self.serializer_class(instance=post,
                                           data=update_data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response({"post": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request: Request, post_id: int) -> Response:
        post = get_object_or_404(Post, id=post_id)
        self.check_object_permissions(request, post)
        post.delete()
        return Response({"detail": "Deleted successfully"},
                        status=status.HTTP_200_OK)


class ListCommentApiView(APIView):
    """
    Class to get a list of comments or create a new one.
    """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request: Request, post_id: int) -> Response:
        comment = request.data.get("comment")
        serializer = self.serializer_class(data=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, post_id=post_id)
        return Response(
            {"comment": serializer.data}, status=status.HTTP_201_CREATED
        )

    def get(self, request: Request, post_id: int) -> Response:
        comments = Post.objects.get(id=post_id).comments
        serializer = self.serializer_class(comments, many=True)
        return Response({"comments": serializer.data},
                        status=status.HTTP_200_OK)


class CommentApiView(APIView):
    """
    Class for CRUD operation to manage comment
    """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly & IsAuthor]

    def get(self, request: Request, comment_id: int) -> Response:
        comment = get_object_or_404(Comment, id=comment_id)
        serializer = self.serializer_class(comment)
        return Response({"comment": serializer.data},
                        status=status.HTTP_200_OK)

    def patch(self, request: Request,
              comment_id: int) -> Response:
        comment = get_object_or_404(Comment, id=comment_id)
        self.check_object_permissions(request, comment)
        update_data = request.data.get("comment")
        serializer = self.serializer_class(instance=comment,
                                           data=update_data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response({"comment": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request: Request,
               comment_id: int) -> Response:
        comment = get_object_or_404(Comment, id=comment_id)
        self.check_object_permissions(request, comment)
        comment.delete()
        return Response({"detail": "Deleted successfully"},
                        status=status.HTTP_200_OK)


class UpvoteApiView(APIView):
    """
    Class to upvote the post
    """

    def post(self, request: Request, post_id: int) -> Response:
        post = get_object_or_404(Post, id=post_id)
        if request.user in post.upvotes.all():
            post.upvotes.remove(request.user)
            message = {"detail": "Post was downvoted"}
        else:
            post.upvotes.add(request.user)
            message = {"detail": "Post was upvoted"}
        return Response(message, status=status.HTTP_200_OK)
