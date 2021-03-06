# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersphones', '0003_auto_20170823_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoviesFullDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(default='', max_length=250, unique=True)),
                ('movie_code', models.CharField(default='', max_length=20, unique=True)),
                ('movie_running_time', models.CharField(default='', max_length=500)),
                ('movie_synopsis', models.CharField(default='', max_length=500)),
                ('movie_genre', models.CharField(default='', max_length=20)),
                ('movie_start_date', models.CharField(default='', max_length=200)),
                ('movie_thumbnail', models.CharField(default='', max_length=200)),
                ('movie_certificate', models.CharField(default='', max_length=200)),
                ('film_code', models.CharField(default='', max_length=500)),
                ('start_time', models.CharField(default='', max_length=200)),
                ('perform_date', models.CharField(default='', max_length=500)),
                ('booking_url', models.CharField(default='', max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Full Movies Details',
            },
        ),
    ]
