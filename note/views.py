from django.http import HttpResponseRedirect
from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, mixins
from .models import Project, TODO
from rest_framework.viewsets import GenericViewSet
from .serializers import ProjectModelSerializer, TODOModelSerializer
from .pagination import ProjectPagination, TODOPagination
from .filters import ProjectFilter
import logging
log = logging.getLogger('projects_log')


class CustomProjectViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                           mixins.ListModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProjectFilter

    def create(self, request, *args, **kwargs):
        self.object = self.get_object()
        log.info(f'todo {self.object.text} was create   d for project {self.object.project.name} by {self.object.user}')
        return super(mixins.CreateModelMixin).create(request, *args, **kwargs)


class CustomTODOViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.ListModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    pagination_class = TODOPagination
    filterset_fields = ['project']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        log.info(f'todo {self.object.text} was deleted from project {self.object.project.name} by {self.object.user}')
        return HttpResponseRedirect('/api/notes/')

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        log.info(f'todo {instance.text} was updated')
        return Response(serializer.data)
