# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-20 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senti', '0004_auto_20160520_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='trends',
            name='count1',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='trends',
            name='count2',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='trends',
            name='count3',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='trends',
            name='count4',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='trends',
            name='count5',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
