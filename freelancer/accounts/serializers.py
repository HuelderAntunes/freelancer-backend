from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import ForgotPassword, PersonalData, BankAccount, File


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


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
