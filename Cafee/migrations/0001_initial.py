# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('chairs_count', models.IntegerField(default=0)),
                ('shape', models.CharField(choices=[('rectangle', 'rectangle'), ('oval', 'oval')], default='rectangle', max_length=20)),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('pos_X', models.IntegerField(default=0)),
                ('pos_y', models.IntegerField(default=0)),
                ('booked', models.TextField(editable=False)),
            ],
        ),
    ]
