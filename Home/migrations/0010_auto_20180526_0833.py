# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-26 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_project_media_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='query',
            old_name='name',
            new_name='subejct',
        ),
        migrations.AddField(
            model_name='query',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='query',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
