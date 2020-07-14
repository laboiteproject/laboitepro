# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-03 22:06
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboite.apps.tasks', '0003_auto_20161224_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apptasks',
            name='asana_project_id',
            field=models.IntegerField(default=None, help_text="Veuillez indiquer l'identifiant du projet Asana dans lequel vous souhaitez travailler", null=True, verbose_name='Identifiant projet Asana'),
        ),
    ]
