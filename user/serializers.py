from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import NoteUser


class UserModelSerializer(ModelSerializer):

    class Meta:
        model = NoteUser
        fields = ('username', 'first_name', 'last_name', 'email')


class UserModelSerializerWithStatus(ModelSerializer):

    class Meta:
        model = NoteUser
        fields = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser')
