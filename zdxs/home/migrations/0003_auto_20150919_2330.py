# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20150912_2214'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('can_check_the_table', 'can_check_the_join_table'),)},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='make_sure_to_join',
            field=models.CharField(default=b'2', max_length=1, blank=True, choices=[(b'1', b'\xe5\x8a\xa0\xe5\x85\xa5'), (b'2', b'\xe8\x80\x83\xe8\x99\x91\xe4\xb8\x80\xe4\xb8\x8b')]),
        ),
    ]
