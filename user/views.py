git from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from .models import NoteUser
from rest_framework.viewsets import GenericViewSet
from .serializers import UserModelSerializer
import logging
log = logging.getLogger('users_log')


class UserCustomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, GenericViewSet):
    queryset = NoteUser.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsAuthenticated]
