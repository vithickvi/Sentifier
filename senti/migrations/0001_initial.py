# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-18 14:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trend1', models.CharField(blank=True, max_length=30)),
                ('trend2', models.CharField(blank=True, max_length=30)),
                ('trend3', models.CharField(blank=True, max_length=30)),
                ('trend4', models.CharField(blank=True, max_length=30)),
                ('trend5', models.CharField(blank=True, max_length=30)),
                ('ctry', models.CharField(blank=True, max_length=30)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='tweethist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet', models.CharField(blank=True, max_length=30)),
                ('status', models.CharField(blank=True, max_length=30)),
                ('maxid', models.CharField(blank=True, max_length=30)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('searchid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='senti.trends')),
            ],
        ),
    ]
