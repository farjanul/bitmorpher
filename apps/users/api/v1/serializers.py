import random
from rest_framework import serializers
from apps.users.models import CustomUserModel
from apps.utils.utils import generate_authentication_token


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUserModel.

    This serializer handles the creation and representation of user instances.
    It ensures that the password is generated using a custom token generator.
    """

    class Meta:
        model = CustomUserModel
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'user_type', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}
