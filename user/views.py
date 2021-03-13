from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import NoteUser
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = NoteUser.objects.all()
    serializer_class = UserModelSerializer
