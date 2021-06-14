from django.db import models

from authentication.models import User


class Post(models.Model):
    """Model for news posts"""

    title = models.CharField(max_length=100)
    link = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(
        User, related_name="post_upvotes", blank=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )


class Comment(models.Model):
    """Model for comments of news post"""

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True)
