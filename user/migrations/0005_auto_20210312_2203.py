# Generated by Django 3.1.7 on 2021-03-12 22:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210304_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('username', models.CharField(max_length=64)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('age', models.IntegerField(default=18)),
            ],
        ),
        migrations.DeleteModel(
            name='Library_User',
        ),
    ]
