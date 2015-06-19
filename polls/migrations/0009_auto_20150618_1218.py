# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20150615_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_related_images',
            name='largeimage',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AddField(
            model_name='post_related_images',
            name='smallimage',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='index_quick_links',
            name='Iquick1_image',
            field=models.CharField(help_text=b'300 x 340', max_length=b'50'),
        ),
        migrations.AlterField(
            model_name='index_quick_links',
            name='Iquick2_image',
            field=models.CharField(help_text=b'300 x 340', max_length=b'50'),
        ),
        migrations.AlterField(
            model_name='index_quick_links',
            name='Iquick3_image',
            field=models.CharField(help_text=b'300 x 340', max_length=b'50'),
        ),
        migrations.AlterField(
            model_name='index_quick_links',
            name='Iquick4_image',
            field=models.CharField(help_text=b'300 x 340', max_length=b'50'),
        ),
        migrations.AlterField(
            model_name='post',
            name='quick1_image',
            field=models.CharField(help_text=b'300 x 340', max_length=b'50'),
        ),
        migrations.AlterField(
            model_name='post',
            name='quick2_image',
            field=models.CharField(help_text=b'300 x 340', max_length=b'50'),
        ),
        migrations.AlterField(
            model_name='post',
            name='quick3_image',
            field=models.CharField(help_text=b'300 x 340', max_length=b'50', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='quick4_image',
            field=models.CharField(help_text=b'300 x 340', max_length=b'50'),
        ),
    ]
