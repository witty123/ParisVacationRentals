# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20150615_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='index_quick_links',
            name='title',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
