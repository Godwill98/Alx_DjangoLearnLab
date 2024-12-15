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
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class ProfileSerializer(serializers.ModelSerializer):
    """Profile Serializer"""

    password = serializers.CharField(write_only=True, required=True)
    token = serializers.SerializerMethodField()


    class Meta:
        model = Profile
        fields = ['user', 'bio', 'phone', 'picture']



