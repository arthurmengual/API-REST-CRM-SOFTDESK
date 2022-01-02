from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from . import serializers
from . import models
from rest_framework.permissions import IsAuthenticated

class UserViewset(ReadOnlyModelViewSet):
    
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.User.objects.all()