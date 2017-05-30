# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-30 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_remove_block_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='blocks',
        ),
        migrations.AddField(
            model_name='block',
            name='pages',
            field=models.ManyToManyField(blank=True, related_name='blocks', to='pages.Page', verbose_name='Pages'),
        ),
        migrations.AlterField(
            model_name='subblock',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_subblocks', to='pages.Block', verbose_name='Block'),
        ),
    ]
