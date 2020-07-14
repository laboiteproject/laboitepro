# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-21 20:40
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boites', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppBikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True, help_text='Indique si cette app est activ\xe9e sur votre bo\xeete', verbose_name='App activ\xe9e ?')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de cr\xe9ation')),
                ('last_activity', models.DateTimeField(auto_now=True, verbose_name='Derni\xe8re activit\xe9')),
                ('provider', models.CharField(choices=[(b'star', 'Star - Rennes'), (b'velib', "V\xe9lib' - Paris")], help_text='Choisissez le service de v\xe9los d\xe9sir\xe9', max_length=64, verbose_name='Fournisseur de donn\xe9es')),
                ('id_station', models.CharField(help_text='Choisissez la station dont vous voulez obtenir les informations', max_length=64, verbose_name='Station')),
                ('station', models.TextField(verbose_name='Nom station')),
                ('slots', models.PositiveIntegerField(null=True, verbose_name='Nombre de places totales')),
                ('bikes', models.PositiveIntegerField(null=True, verbose_name='Nombre de v\xe9los disponibles')),
                ('status', models.NullBooleanField(verbose_name='En fonctionnement ?')),
                ('boite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boites.Boite', verbose_name='Bo\xeete')),
            ],
            options={
                'verbose_name': 'Configuration : v\xe9los',
                'verbose_name_plural': 'Configurations : v\xe9los',
            },
        ),
    ]
