from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Project, TODO, NoteUser


class ProjectModelSerializer(ModelSerializer):
    users = StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Project
        exclude = ['uuid', 'id']


class ProjectModelSerializerBase(ModelSerializer):
    class Meta:
        model = Project
        exclude = ['uuid', 'id']


class TODOModelSerializer(ModelSerializer):
    project = StringRelatedField()
    creator = StringRelatedField()

    class Meta:
        model = TODO
        fields = ['project', 'creator', 'text']


class CreateTODOModelSerializer(ModelSerializer):

    class Meta:
        model = TODO
        fields = ['project', 'creator', 'text']
