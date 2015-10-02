# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='has_been_deal_with',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='make_sure_to_join',
            field=models.CharField(blank=True, max_length=1, choices=[(b'1', b'\xe5\x8a\xa0\xe5\x85\xa5'), (b'2', b'\xe8\x80\x83\xe8\x99\x91\xe4\xb8\x80\xe4\xb8\x8b')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='team',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
