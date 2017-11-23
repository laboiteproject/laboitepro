# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 08:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boites', '0002_auto_20161224_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveSmallIntegerField(default=5000, help_text='Veuillez saisir une dur\xe9e durant laquelle la tuile sera affich\xe9e (en millisecondes)', verbose_name="Dur\xe9e d'affichage de la tuile")),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de cr\xe9ation')),
                ('boite', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='boites.Boite', verbose_name='Bo\xeete')),
            ],
        ),
        migrations.CreateModel(
            name='TileApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.PositiveSmallIntegerField(default=0, help_text="Veuillez indiquer la position en x de l'app sur la tuile (en pixels)", verbose_name='Position x')),
                ('y', models.PositiveSmallIntegerField(default=0, help_text="Veuillez indiquer la position en y de l'app sur la tuile (en pixels)", verbose_name='Position y')),
                ('tile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='boites.Tile', verbose_name='Tuile')),
            ],
        ),
    ]