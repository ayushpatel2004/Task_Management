# Generated by Django 4.1.2 on 2023-01-14 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskHub', '0004_remove_tasks_groupname_groups_taskcompleted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='percentage',
            field=models.FloatField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='tasks',
            name='points',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
