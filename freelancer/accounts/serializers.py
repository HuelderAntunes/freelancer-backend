from rest_framework import serializers
from .models import ForgotPassword, PersonalData, BankAccount, File


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class RecoverPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField()
    new_password = serializers.CharField()


class PersonalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalData
        fields = '__all__'


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['name', 'path']
        read_only_fields = ['created_at', 'updated_at']


class RoleSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
