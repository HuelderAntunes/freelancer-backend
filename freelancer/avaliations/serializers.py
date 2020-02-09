from rest_framework.serializers import ModelSerializer
from .models import Avaliation, AvaliationField, AvaliationValue


class AvaliationSerializer(ModelSerializer):
    class Meta:
        model = Avaliation
        fields = ['rated', 'evaluator', 'created_date', 'updated_date']

        read_only = ['evaluator', 'created_date', 'updated_date']


class AvaliationValueSerializer(ModelSerializer):
    class Meta:
        model = AvaliationValue
        fields = ['avaliation', 'avaliation_field', 'rank']


class AvaliationFieldSerializer(ModelSerializer):
    class Meta:
        model = AvaliationField
        fields = ['name', 'description']
