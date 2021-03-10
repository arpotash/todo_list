# Generated by Django 3.1.7 on 2021-03-04 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_auto_20210303_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library_User',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=64, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
