# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-26 08:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_auto_20180526_0833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='query',
            old_name='subejct',
            new_name='subject',
        ),
    ]