from rest_framework import viewsets, permissions, filters, generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth import get_user_model
from .serializers import PostSerializer


User = get_user_model()

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.method in permissions.SAFE_METHODS

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Task 2: Feed View

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()  # ← define variable exactly as test expects
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
