from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'bio', 'profile_picture')

    def create(self, validated_data):
        # Pop optional fields to handle defaults
        bio = validated_data.pop('bio', '')
        profile_picture = validated_data.pop('profile_picture', None)

        # Create user using create_user (handles password hashing)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=bio,
            profile_picture=profile_picture
        )

        # Create token for the user
        Token.objects.create(user=user)
        return user
