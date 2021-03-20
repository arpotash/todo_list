from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins, viewsets
from .models import NoteUser
from .serializers import UserModelSerializer
import logging
log = logging.getLogger('users_log')


class UserCustomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    queryset = NoteUser.objects.all()
    serializer_class = UserModelSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        log.info(f'user {instance.username} was updated')
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        objects = self.get_queryset()
        serializer = UserModelSerializer(objects, many=True)
        log.info(f'get list - {serializer.data}')
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        log.info(f'get object - {serializer.data}')
        return Response(serializer.data)
