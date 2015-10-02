# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('summury', models.CharField(max_length=300)),
                ('data_time', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('counts', models.IntegerField(default=0)),
                ('editor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('can_write', 'can write the blog'), ('can_read', 'can read the blog')),
            },
        ),
    ]
