# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-19 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_auto_20180519_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='media_type',
            field=models.BooleanField(default=0),
        ),
    ]