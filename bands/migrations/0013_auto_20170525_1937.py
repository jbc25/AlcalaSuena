# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-25 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0012_auto_20170525_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='city',
            field=models.CharField(blank=True, max_length=140, null=True, verbose_name='Ciudad'),
        ),
    ]