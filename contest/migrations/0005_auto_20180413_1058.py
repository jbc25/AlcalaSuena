# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-13 10:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0004_auto_20180413_1054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contestjuryvote',
            options={'ordering': ['band'], 'verbose_name': 'Voto del jurado', 'verbose_name_plural': 'Votos del jurado'},
        ),
    ]
