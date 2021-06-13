from rest_framework import serializers
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializer for user registration and creation a new one"""

    password = serializers.CharField(
        max_length=64, min_length=8, write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "token"]

    def create(self, validated_data):
        """Create new user with validated data"""
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=32, read_only=True)
    password = serializers.CharField(max_length=64, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, attrs):
        email = data.get("email", None)
        password = data.get("password", None)
