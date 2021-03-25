from django_filters import rest_framework as filters
from .models import Project, TODO, NoteUser


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class TODOFilter(filters.FilterSet):
    project = filters.CharFilter

    class Meta:
        model = TODO
        fields = ['project']
