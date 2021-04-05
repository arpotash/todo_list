from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser


class NoteUser(AbstractUser):
    email = models.EmailField(unique=True)
    uuid = models.UUIDField(default=uuid4)
    age = models.IntegerField(default=18)

    class Meta:
        verbose_name = "User"

    def __str__(self):
        return self.username
