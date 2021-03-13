from rest_framework.serializers import HyperlinkedModelSerializer
from .models import NoteUser


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = NoteUser
        fields = 'username', 'first_name', 'last_name', 'email'
