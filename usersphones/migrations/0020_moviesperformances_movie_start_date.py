# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-08 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersphones', '0019_auto_20171108_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviesperformances',
            name='movie_start_date',
            field=models.CharField(default='', max_length=200),
        ),
    ]