# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 11:56
from __future__ import unicode_literals

import apps.pages.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('media', models.FileField(upload_to=apps.pages.models.upload_to, verbose_name='File')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('order', models.PositiveSmallIntegerField(blank=True, default=500, null=True, verbose_name='Order')),
                ('public', models.BooleanField(default=True, verbose_name='Public')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'ordering': ['order', 'name'],
                'verbose_name': 'Media',
                'verbose_name_plural': 'Media',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('header', models.CharField(max_length=256, verbose_name='Header')),
                ('keywords', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Keywords')),
                ('description', models.CharField(blank=True, max_length=2048, null=True, verbose_name='Description')),
                ('intro', models.TextField(blank=True, null=True, verbose_name='Intro')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Text')),
                ('img', models.FileField(blank=True, upload_to=b'img/pages', verbose_name='Image')),
                ('per_page', models.IntegerField(default=10, help_text='The maximum number of items to include on a page', verbose_name='Items per page')),
                ('template', models.CharField(blank=True, max_length=32, null=True, verbose_name='Template')),
                ('level', models.IntegerField(default=0, editable=False, verbose_name='Level')),
                ('order', models.IntegerField(blank=True, default=500, null=True, verbose_name='Order')),
                ('real_order', models.IntegerField(blank=True, default=500, editable=False, null=True, verbose_name='Real Order')),
                ('slug', models.CharField(default=b'#', max_length=256, verbose_name='Slug')),
                ('url', models.CharField(editable=False, max_length=1024, verbose_name='URL')),
                ('main', models.BooleanField(default=False, verbose_name='Main')),
                ('public', models.BooleanField(default=True, verbose_name='Public')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='pages.Page', verbose_name='Parent')),
                ('sites', models.ManyToManyField(blank=True, related_name='pagess', to='sites.Site', verbose_name='Sites')),
            ],
            options={
                'ordering': ['real_order', '-created_at'],
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('slug', models.SlugField(help_text='A slug is the part of a URL which identifies a page using human-readable keywords', max_length=128, verbose_name='Slug')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='page',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='pages', to='pages.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='media',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media', to='pages.Page', verbose_name='Page'),
        ),
    ]
