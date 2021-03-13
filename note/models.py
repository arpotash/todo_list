from django.db import models
from user.models import NoteUser
from uuid import uuid4
from datetime import datetime

# Create your models here.


class Project(models.Model):
    uuid = models.UUIDField(default=uuid4)
    users = models.ManyToManyField(NoteUser, related_name='owner')
    name = models.CharField(max_length=64)
    url = models.URLField(verbose_name='repository_url')

    def __str__(self):
        return self.name


class TODO(models.Model):
    uuid = models.UUIDField(default=uuid4)
    project = models.ForeignKey(Project, related_name='project', on_delete=models.CASCADE)
    text = models.TextField(max_length=512)
    date_create = models.DateTimeField(verbose_name='create_at', auto_now_add=True)
    date_update = models.DateTimeField(verbose_name='update_at', auto_now_add=True)
    user = models.ForeignKey(NoteUser, related_name='creator', on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
