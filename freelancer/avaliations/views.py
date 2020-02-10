from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import permissions
from .models import *
from .serializers import *
from rest_framework.response import Response


class AvaliationViewSet(ModelViewSet):
    queryset = Avaliation.objects.all().order_by('-id')
    serializer_class = AvaliationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        rated = AvaliationSerializer(data=request.data)
        if(rated.is_valid()):
            avaliation = Avaliation.objects.create(evaluator=request.user,
                                                   rated=request.data)
            return Response(AvaliationSerializer(avaliation))

        return Response({'error': 'Invalid request data.'})


class AvaliationValueViewSet(ModelViewSet):
    queryset = AvaliationValue.objects.all()
    serializer_class = AvaliationValueSerializer
    permission_classes = [permissions.IsAuthenticated]


class AvaliationFieldViewSet(ReadOnlyModelViewSet):
    queryset = AvaliationField.objects.all()
    serializer_class = AvaliationFieldSerializer
    permission_classes = [permissions.IsAuthenticated]
