# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-09 10:25
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boites', '0009_pushbutton'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pushbutton',
            name='event_name',
        ),
    ]
