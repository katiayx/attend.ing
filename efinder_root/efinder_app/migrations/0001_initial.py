# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-03 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=220)),
                ('description', models.TextField()),
                ('start_time', models.CharField(max_length=50)),
                ('end_time', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=200)),
                ('is_free', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
