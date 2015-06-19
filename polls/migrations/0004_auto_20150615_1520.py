# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20150615_1515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='index_quick_links',
            options={'verbose_name_plural': 'Index quick links'},
        ),
        migrations.AddField(
            model_name='index_quick_links',
            name='current',
            field=models.BooleanField(default=True, verbose_name=b'current'),
        ),
    ]
