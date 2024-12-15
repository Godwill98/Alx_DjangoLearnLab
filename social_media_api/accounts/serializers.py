from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import CustomUser, Profile


class CustomUserSerializer(serializers.ModelSerializer):
    """Custom User Serializer"""

    password = serializers.CharField(write_only=True, required=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'token']

    def create(self, validated_data):
        # Create the user using `get_user_model`
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Generate a token for the user
        Token.objects.create(user=user)
        return user

    def get_token(self, obj):
        # Retrieve or create the token for the user
        token, _ = Token.objects.get_or_create(user=obj)
        return token.key


class ProfileSerializer(serializers.ModelSerializer):
    """Profile Serializer"""

    class Meta:
        model = Profile
        fields = ['user', 'bio', 'phone', 'picture']
