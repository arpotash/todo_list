from django.http import HttpResponseRedirect
from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Project, TODO
from rest_framework.viewsets import GenericViewSet
from .serializers import ProjectModelSerializer, TODOModelSerializer
from .pagination import ProjectPagination, TODOPagination
from .filters import ProjectFilter
import logging
log = logging.getLogger('projects_log')


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProjectFilter


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    pagination_class = TODOPagination
    filterset_fields = ['project']

    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
