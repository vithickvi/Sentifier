# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-21 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senti', '0005_auto_20160520_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweethist',
            name='loca',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]