from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User


class Library_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid4)

    email = models.CharField(max_length=64, unique=True)