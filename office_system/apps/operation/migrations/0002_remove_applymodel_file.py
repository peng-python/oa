# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-17 05:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applymodel',
            name='file',
        ),
    ]