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
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=200)),
                ('category_image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('summury', models.CharField(max_length=300)),
                ('data_time', models.DateTimeField(auto_now_add=True)),
                ('data', models.TextField()),
                ('counts', models.IntegerField(default=0)),
                ('data_category', models.ForeignKey(to='data.Category')),
                ('editor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('can_write', 'can write the data'),),
            },
        ),
        migrations.CreateModel(
            name='DataComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('editor', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('data_time', models.DateTimeField(auto_now_add=True)),
                ('link', models.ForeignKey(to='data.Data')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='tag',
            field=models.ForeignKey(to='data.Tag'),
        ),
    ]
