# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-03 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('facebook_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('pic', models.CharField(max_length=100)),
                ('high_score', models.IntegerField()),
            ],
        ),
    ]
