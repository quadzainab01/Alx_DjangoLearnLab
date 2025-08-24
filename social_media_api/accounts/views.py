from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        # Use the serializer to create the user
        response = super().create(request, *args, **kwargs)

        # Generate token for the created user
        token = Token.objects.get(user_id=response.data['id'])
        response.data['token'] = token.key

        return response
