from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField(max_length=512)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ("author", "date")


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ("post", "author", "date")
