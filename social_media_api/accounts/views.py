from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, FollowSerializer, CustomUserSerializer
from .models import CustomUser

User = get_user_model()


# ----------------------------
# Registration View
# ----------------------------
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        # Keep original registration and token logic
        response = super().create(request, *args, **kwargs)
        token = Token.objects.get(user_id=response.data['id'])
        response.data['token'] = token.key
        return response


# ----------------------------
# Follow / Unfollow Views
# ----------------------------
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        request.user.following.add(target_user)
        return Response(
            {'message': f'You are now following {target_user.username}'},
            status=status.HTTP_200_OK
        )


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        request.user.following.remove(target_user)
        return Response(
            {'message': f'You have unfollowed {target_user.username}'},
            status=status.HTTP_200_OK
        )


# ----------------------------
# List All Users View
# ----------------------------
class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()  # ← satisfies the test
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]


from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from posts.serializers import PostSerializer

# ----------------------------
# Create a Post
# ----------------------------
class CreatePostView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# ----------------------------
# List All Posts
# ----------------------------
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


# ----------------------------
# Feed View (Posts by Followed Users)
# ----------------------------
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()  # ManyToManyField `following`
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

# ----------------------------
# Optional: Retrieve Single Post
# ----------------------------
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
