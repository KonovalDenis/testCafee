# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cafee', '0007_auto_20171116_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='booked',
            field=models.TextField(blank=True, default=''),
        ),
    ]