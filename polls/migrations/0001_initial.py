# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(default=b'the-category', max_length=100)),
                ('info', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(default=b'the-url', help_text=b'url for post', max_length=100)),
                ('pub_date', models.DateField(verbose_name=b'date published')),
                ('updated_date', models.DateField(default=datetime.date.today, verbose_name=b'date updated')),
                ('is_enabled', models.BooleanField(verbose_name=b'is enabled')),
                ('is_article', models.BooleanField(default=True, verbose_name=b'is article')),
                ('is_guide', models.BooleanField(default=True, verbose_name=b'is guide')),
                ('body', ckeditor.fields.RichTextField(help_text=b'image url: /media/"url on image upload page"')),
                ('meta_title', models.TextField(default=b'')),
                ('meta_description', models.TextField(default=b'')),
                ('meta_keywords', models.TextField(default=b'')),
                ('meta_canonical', models.URLField(default=b'')),
                ('quick1', models.URLField(verbose_name=b'quick1')),
                ('quick1_image', models.ImageField(upload_to=b'img/%Y/%m/%d')),
                ('quick2', models.URLField(verbose_name=b'quick2')),
                ('quick2_image', models.ImageField(upload_to=b'img/%Y/%m/%d')),
                ('quick3', models.URLField(verbose_name=b'quick3')),
                ('quick3_image', models.ImageField(upload_to=b'img/%Y/%m/%d')),
                ('quick4', models.URLField(verbose_name=b'quick4')),
                ('quick4_image', models.ImageField(upload_to=b'img/%Y/%m/%d')),
                ('categories', models.ManyToManyField(to='polls.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Post_related_images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to=b'img/%Y/%m/%d')),
                ('post', models.ForeignKey(related_name='images', to='polls.Post')),
            ],
            options={
                'verbose_name_plural': 'Post related images',
            },
        ),
    ]
