# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-02 13:12
from __future__ import unicode_literals

import bands.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0018_settings'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=bands.helpers.RandomFileName('news/'), verbose_name='Imagen de noticia')),
                ('btn_text', models.CharField(blank=True, max_length=200, null=True)),
                ('btn_link', models.CharField(blank=True, max_length=200, null=True)),
                ('native_code', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('caducity', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['start_date', 'end_date'],
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
            },
        ),
        migrations.AlterField(
            model_name='band',
            name='band_image',
            field=models.ImageField(blank=True, null=True, upload_to=bands.helpers.RandomFileName('band/'), verbose_name='Imagen de cabecera'),
        ),
        migrations.AlterField(
            model_name='band',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descripci\xf3n'),
        ),
        migrations.AlterField(
            model_name='band',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=bands.helpers.RandomFileName('band/'), verbose_name='Imagen principal'),
        ),
    ]
