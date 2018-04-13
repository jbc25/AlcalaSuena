# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-13 10:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contest', '0003_contestband_rider_doc'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContestJuryVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(null=True, verbose_name='Timestamp')),
                ('vote', models.IntegerField(default=0, verbose_name='Voto')),
            ],
            options={
                'ordering': ['band'],
                'verbose_name': 'Miembro de banda',
                'verbose_name_plural': 'Miembros de bandas',
            },
        ),
        migrations.AlterField(
            model_name='contestband',
            name='embed_code',
            field=models.TextField(blank=True, null=True, verbose_name='C\xf3dido embed (enlace o iframe) para escucha (Bandcamp, Soundcloud, Spotify...)'),
        ),
        migrations.AlterField(
            model_name='contestband',
            name='embed_media',
            field=models.TextField(blank=True, null=True, verbose_name='C\xf3dido embed (enlace o iframe) de v\xeddeo (Youtube, Vimeo...)'),
        ),
        migrations.AddField(
            model_name='contestjuryvote',
            name='band',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jury_votes', to='contest.ContestBand', verbose_name='Banda'),
        ),
        migrations.AddField(
            model_name='contestjuryvote',
            name='voted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contest_votes', to=settings.AUTH_USER_MODEL, verbose_name='Jurado'),
        ),
    ]
