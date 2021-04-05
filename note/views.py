from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Project, TODO
from .serializers import ProjectModelSerializer, TODOModelSerializer, ProjectModelSerializerBase, \
    CreateTODOModelSerializer
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = [IsAuthenticated]


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    pagination_class = TODOPagination
    filterset_fields = ['project']
    serializer_class = TODOModelSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TODOModelSerializer
        return CreateTODOModelSerializer

    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
