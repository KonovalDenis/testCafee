# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cafee', '0005_auto_20171115_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='shape',
            field=models.IntegerField(choices=[(1, 'rectangle'), (0, 'oval')], default='rectangle'),
        ),
    ]
