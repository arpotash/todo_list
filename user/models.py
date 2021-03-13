from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User


class NoteUser(models.Model):
    uuid = models.UUIDField(default=uuid4)
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    age = models.IntegerField(default=18)

    def __str__(self):
        return self.username
