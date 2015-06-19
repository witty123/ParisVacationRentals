# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='quick1',
            field=models.SlugField(help_text=b'url for post', verbose_name=b'quick1'),
        ),
        migrations.AlterField(
            model_name='post',
            name='quick2',
            field=models.SlugField(help_text=b'url for post', verbose_name=b'quick2'),
        ),
        migrations.AlterField(
            model_name='post',
            name='quick3',
            field=models.SlugField(help_text=b'url for post', verbose_name=b'quick3'),
        ),
        migrations.AlterField(
            model_name='post',
            name='quick4',
            field=models.SlugField(help_text=b'url for post', verbose_name=b'quick4'),
        ),
    ]
