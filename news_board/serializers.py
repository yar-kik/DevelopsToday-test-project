from rest_framework import serializers

from news_board.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    """Class for news posts serialization/deserialization"""

    total_upvotes = serializers.SerializerMethodField(read_only=True)
    total_comments = serializers.SerializerMethodField(read_only=True)

    def get_total_upvotes(self, post: Post) -> int:
        return post.upvotes.count()

    def get_total_comments(self, post: Post) -> int:
        return post.comments.count()

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "link",
            "created",
            "total_upvotes",
            "author",
            "total_comments",
        )
        read_only_fields = (
            "id",
            "created",
            "author",
            "total_upvotes",
            "total_comments",
        )


class CommentSerializer(serializers.ModelSerializer):
    """Class for comments of news posts serialization/deserialization"""

    class Meta:
        model = Comment
        fields = ("id", "author", "content", "created", "post")
        read_only_fields = ("id", "created", "author", "post")
