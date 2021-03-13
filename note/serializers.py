from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Project, TODO
from user.serializers import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):
    users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ['name', 'url', 'users']


class TODOModelSerializer(ModelSerializer):
    project = ProjectModelSerializer()
    user = StringRelatedField()

    class Meta:
        model = TODO
        exclude = ['uuid', 'id']
