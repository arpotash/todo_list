# Generated by Django 3.1.7 on 2021-03-19 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210312_2203'),
        ('note', '0011_auto_20210319_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='note.project'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='creator', to='user.noteuser'),
        ),
    ]
