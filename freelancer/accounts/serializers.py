from rest_framework import serializers
from .models import ForgotPassword


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class RecoverPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField()
    new_password = serializers.CharField()
