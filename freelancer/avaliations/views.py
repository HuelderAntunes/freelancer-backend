from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import permissions
from .models import *
from .serializers import *
from rest_framework.response import Response


def AvaliationViewSet(ModelViewSet):
    queryset = Avaliation.objects.all().order_by('-id')
    serializer_class = AvaliationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        rated = AvaliationSerializer(data=request.data)
        if(rated.is_valid()):
            avaliation = Avaliation.objects.create(evaluator=request.user
                                                   rated=request.data)
            return Response(AvaliationSerializer(avaliation))

        return Response({'error': 'Invalid request data.'})


def AvaliationValueViewSet(ModelViewSet):
    model = AvaliationValue
    serializer_class = AvaliationValueSerializer
    permission_classes = [permissions.IsAuthenticated]


def AvaliationFieldViewSet(ReadOnlyModelViewSet):
    model = AvaliationField
    serializer_class = AvaliationFieldSerializer
    permission_classes = [permissions.IsAuthenticated]
