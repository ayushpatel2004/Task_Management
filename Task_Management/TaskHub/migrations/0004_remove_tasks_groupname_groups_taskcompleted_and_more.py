# Generated by Django 4.1.2 on 2023-01-14 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskHub', '0003_alter_groups_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='groupname',
        ),
        migrations.AddField(
            model_name='groups',
            name='taskcompleted',
            field=models.IntegerField(default=0, max_length=1000000),
        ),
        migrations.AddField(
            model_name='groups',
            name='tasknum',
            field=models.IntegerField(default=0, max_length=1000000),
        ),
        migrations.AddField(
            model_name='groups',
            name='tasks',
            field=models.ManyToManyField(related_name='groups', to='TaskHub.tasks'),
        ),
    ]
