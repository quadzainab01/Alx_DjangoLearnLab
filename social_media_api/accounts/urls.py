from django.urls import path
from .views import (
    RegisterView,
    FollowUserView,
    UnfollowUserView,
    UserListView,
    CreatePostView,
    PostListView,
    FeedView,
    PostDetailView
)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),

    # Users
    path('users/', UserListView.as_view(), name='user-list'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),

    # Posts
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/create/', CreatePostView.as_view(), name='post-create'),
    path('posts/feed/', FeedView.as_view(), name='post-feed'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
