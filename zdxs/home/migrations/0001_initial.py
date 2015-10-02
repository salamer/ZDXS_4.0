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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('has_profile', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('sex', models.CharField(max_length=1, choices=[(b'M', b'\xe7\x94\xb7'), (b'W', b'\xe5\xa5\xb3'), (b'U', b'\xe4\xb8\x8d\xe6\x98\x8e')])),
                ('subject', models.CharField(max_length=150, blank=True)),
                ('classname', models.CharField(max_length=100, blank=True)),
                ('birthday', models.CharField(max_length=100, blank=True)),
                ('race', models.CharField(max_length=50, blank=True)),
                ('avatar', models.ImageField(upload_to=b'avatar')),
                ('has_avatar', models.BooleanField(default=False)),
                ('contact', models.CharField(max_length=400, blank=True)),
                ('introduction', models.TextField(blank=True)),
                ('something', models.TextField(blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
