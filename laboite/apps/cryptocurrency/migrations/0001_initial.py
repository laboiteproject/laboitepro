# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-03 23:41
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boites', '0011_tile_brightness'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppCryptocurrency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('enabled', models.BooleanField(default=True, help_text='Indique si cette app est activée sur votre boîte', verbose_name='App activée ?')),
                ('last_activity', models.DateTimeField(null=True, verbose_name='Dernière activité')),
                ('cryptocurrency', models.CharField(choices=[('bitcoin', 'Bitcoin'), ('ethereum', 'Ethereum'), ('bitcoin-cash', 'Bitcoin Cash'), ('ripple', 'Ripple'), ('dash', 'Dash')], default='bitcoin', help_text='Veuillez indiquer la crypto-monnaie que vous souhaitez convertir', max_length=16, verbose_name='Crypto-monnaie')),
                ('currency', models.CharField(choices=[('USD', 'Dollars'), ('EUR', 'Euros')], default='EUR', help_text='Veuillez indiquer la devise dans laquelle vous souhaitez convertir', max_length=8, verbose_name='Monnaie')),
                ('value', models.PositiveSmallIntegerField(default=0, verbose_name='Valeur')),
                ('boite', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='boites.Boite', verbose_name='Boîte')),
            ],
            options={
                'verbose_name': 'Configuration : facebook likes',
                'verbose_name_plural': 'Configurations : facebook likes',
            },
        ),
    ]
