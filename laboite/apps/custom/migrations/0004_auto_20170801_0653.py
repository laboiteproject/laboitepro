# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-01 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboite.apps.custom', '0003_auto_20170730_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appcustom',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='appcustom',
            name='message',
        ),
        migrations.AddField(
            model_name='appcustom',
            name='bitmap0',
            field=models.TextField(blank=True, default='', max_length=1024, verbose_name='Ic\xf4ne'),
        ),
        migrations.AddField(
            model_name='appcustom',
            name='bitmap1',
            field=models.TextField(blank=True, default='', max_length=1024, verbose_name='Ic\xf4ne'),
        ),
        migrations.AddField(
            model_name='appcustom',
            name='bitmap2',
            field=models.TextField(blank=True, default='', max_length=1024, verbose_name='Ic\xf4ne'),
        ),
        migrations.AddField(
            model_name='appcustom',
            name='bitmap3',
            field=models.TextField(blank=True, default='', max_length=1024, verbose_name='Ic\xf4ne'),
        ),
        migrations.AddField(
            model_name='appcustom',
            name='bitmap4',
            field=models.TextField(blank=True, default='', max_length=1024, verbose_name='Ic\xf4ne'),
        ),
    ]
