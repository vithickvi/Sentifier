# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-18 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senti', '0002_trendsfull'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trendsfull',
            name='count',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
