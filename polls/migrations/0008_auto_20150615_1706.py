# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20150615_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index_quick_links',
            name='Iquick1_image',
            field=models.URLField(help_text=b'300 x 340'),
        ),
        migrations.AlterField(
            model_name='index_quick_links',
            name='Iquick2_image',
            field=models.URLField(help_text=b'300 x 340'),
        ),
        migrations.AlterField(
            model_name='index_quick_links',
            name='Iquick3_image',
            field=models.URLField(help_text=b'300 x 340'),
        ),
        migrations.AlterField(
            model_name='index_quick_links',
            name='Iquick4_image',
            field=models.URLField(help_text=b'300 x 340'),
        ),
        migrations.AlterField(
            model_name='post',
            name='quick1',
            field=models.SlugField(help_text=b'url for post', verbose_name=b'quick1'),
        ),
        migrations.AlterField(
            model_name='post',
            name='quick1_image',
            field=models.URLField(help_text=b'300 x 340'),
        ),
        migrations.AlterField(
            model_name='post',
            name='quick2',
            field=models.SlugField(help_text=b'url for post', verbose_name=b'quick2'),
        ),
        migrations.AlterField(
            model_name='post',
            name='quick2_image',
            field=models.URLField(help_text=b'300 x 340'),
        ),
        migrations.AlterField(
            model_name='post',
            name='quick3',
            field=models.SlugField(help_text=b'url for post', verbose_name=b'quick3'),
        ),
        migrations.AlterField(
            model_name='post',
            name='quick3_image',
            field=models.URLField(help_text=b'300 x 340'),
        ),
        migrations.AlterField(
            model_name='post',
            name='quick4',
            field=models.SlugField(help_text=b'url for post', verbose_name=b'quick4'),
        ),
        migrations.AlterField(
            model_name='post',
            name='quick4_image',
            field=models.URLField(help_text=b'300 x 340'),
        ),
    ]
