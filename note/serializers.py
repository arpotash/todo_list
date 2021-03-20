from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Project, TODO, NoteUser
from user.serializers import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):
    users = StringRelatedField(many=True)

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

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