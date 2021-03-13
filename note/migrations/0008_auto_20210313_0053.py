# Generated by Django 3.1.7 on 2021-03-13 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0007_todo_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(verbose_name='repository_url'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create_at'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='date_update',
            field=models.DateTimeField(auto_now_add=True, verbose_name='update_at'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
