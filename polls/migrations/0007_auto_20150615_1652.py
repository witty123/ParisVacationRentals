# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20150615_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='index_quick_links',
            name='Iquick1_title',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='index_quick_links',
            name='Iquick2_title',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='index_quick_links',
            name='Iquick3_title',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='index_quick_links',
            name='Iquick4_title',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='quick1_title',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='quick2_title',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='quick3_title',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='quick4_title',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
