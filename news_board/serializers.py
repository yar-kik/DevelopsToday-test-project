from rest_framework import serializers

from news_board.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    """Class for news posts serialization/deserialization"""

    total_upvotes = serializers.SerializerMethodField(read_only=True)

    def get_total_upvotes(self, post: Post):
        print(post.upvotes)
        return post.upvotes.count()

    class Meta:
        model = Post
        fields = ("id", "title", "link", "created", "total_upvotes", "author")
        read_only_fields = ("author", "total_upvotes")


class CommentSerializer(serializers.ModelSerializer):
    """Class for comments of news posts serialization/deserialization"""

    class Meta:
        model = Comment
        fields = ("id", "author", "content", "created", "post")
        read_only_fields = ("author", "post")
