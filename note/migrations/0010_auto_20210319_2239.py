# Generated by Django 3.1.7 on 2021-03-19 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210312_2203'),
        ('note', '0009_auto_20210319_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='username',
            field=models.ManyToManyField(to='user.NoteUser'),
        ),
    ]
