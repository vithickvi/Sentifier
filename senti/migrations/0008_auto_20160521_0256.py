# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-21 02:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('senti', '0007_remove_tweethist_searchid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweethist',
            old_name='loca',
            new_name='searchreq',
        ),
    ]
