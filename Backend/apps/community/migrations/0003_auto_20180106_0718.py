# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-06 07:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20180106_0639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='id_proyecto',
        ),
        migrations.DeleteModel(
            name='like',
        ),
        migrations.DeleteModel(
            name='publicacion',
        ),
        migrations.DeleteModel(
            name='usuarios',
        ),
        migrations.DeleteModel(
            name='comentario',
        ),
        migrations.DeleteModel(
            name='proyecto',
        ),
    ]
