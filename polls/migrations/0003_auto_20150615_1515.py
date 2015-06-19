# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150615_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index_quick_links',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Iquick1', models.SlugField(help_text=b'url for post', verbose_name=b'Iquick1')),
                ('Iquick1_image', models.ImageField(help_text=b'300 x 340', upload_to=b'img/%Y/%m/%d')),
                ('Iquick2', models.SlugField(help_text=b'url for post', verbose_name=b'Iquick2')),
                ('Iquick2_image', models.ImageField(help_text=b'300 x 340', upload_to=b'img/%Y/%m/%d')),
                ('Iquick3', models.SlugField(help_text=b'url for post', verbose_name=b'Iquick3')),
                ('Iquick3_image', models.ImageField(help_text=b'300 x 340', upload_to=b'img/%Y/%m/%d')),
                ('Iquick4', models.SlugField(help_text=b'url for post', verbose_name=b'Iquick4')),
                ('Iquick4_image', models.ImageField(help_text=b'300 x 340', upload_to=b'img/%Y/%m/%d')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='quick1_image',
            field=models.ImageField(help_text=b'300 x 340', upload_to=b'img/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='post',
            name='quick2_image',
            field=models.ImageField(help_text=b'300 x 340', upload_to=b'img/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='post',
            name='quick3_image',
            field=models.ImageField(help_text=b'300 x 340', upload_to=b'img/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='post',
            name='quick4_image',
            field=models.ImageField(help_text=b'300 x 340', upload_to=b'img/%Y/%m/%d'),
        ),
    ]
