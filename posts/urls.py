from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:post_id>", views.detail, name="detail"),
    path("post/", views.make_post, name="post"),
    # Authentication
    path("authenticate_user/", views.authenticate_user, name="authenticate_user"),
    path("login/", views.user_login, name="login"),
    path("register/", views.user_registration, name="register"),
    path("logout/", views.user_logout, name="logout"),
]
