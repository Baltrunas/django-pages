# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 11:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import helpful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_page_blocks'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=2048, null=True, verbose_name='Description')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Text')),
                ('image', models.FileField(blank=True, null=True, upload_to=helpful.fields.upload_to, verbose_name='Image')),
                ('order', models.PositiveIntegerField(default=500, verbose_name='Sort ordering')),
                ('public', models.BooleanField(default=True, verbose_name='Public')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Sub block',
                'verbose_name_plural': 'Sub blocks',
            },
        ),
        migrations.AddField(
            model_name='block',
            name='template',
            field=models.CharField(blank=True, max_length=124, null=True, verbose_name='Template'),
        ),
        migrations.AlterField(
            model_name='page',
            name='blocks',
            field=models.ManyToManyField(blank=True, related_name='pages', to='pages.Block', verbose_name='Blocks'),
        ),
        migrations.AddField(
            model_name='subblock',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subblocks', to='pages.Block', verbose_name='Block'),
        ),
    ]
