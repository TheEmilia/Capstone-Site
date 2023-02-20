from django.shortcuts import render, get_object_or_404
from .models import CommentForm, Post, PostForm

# Authentication
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# index
def index(request):
    latest_post_list = Post.objects.order_by("-date")[:8]
    context = {"latest_post_list": latest_post_list}
    return render(request, "index.html", context)


# detail
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return HttpResponseRedirect("#")
    else:
        form = CommentForm()
    context = {"post": post, "form": form}
    return render(request, "detail.html", context)


def make_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.title = form.cleaned_data.get("title")
            # post.content = form.cleaned_data.get("content")
            post.save()
            return HttpResponseRedirect(reverse("posts:index"))
    else:
        form = PostForm()
    return render(request, "post.html", {"form": form})


# Authentication


# user_authentication
def authenticate_user(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(reverse("posts:login"))
    else:
        login(request, user)
        return HttpResponseRedirect(reverse("posts:index"))


# user_login
def user_login(request):
    return render(request, "login.html")


# user_registration
def user_registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse("posts:index"))
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


# user_logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("posts:index"))
