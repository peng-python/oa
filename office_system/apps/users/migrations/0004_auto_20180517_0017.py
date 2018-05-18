# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-17 00:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180517_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='education',
            field=models.CharField(choices=[('college', '大专'), ('undergraduate', '本科'), ('graduate', '研究生'), ('doctor', '博士生')], default='job', max_length=6, verbose_name='学历'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='policital_status',
            field=models.CharField(choices=[('party', '党员'), ('masses', '群众'), ('other', '其他')], default='masses', max_length=6, verbose_name='政治面貌'),
        ),
    ]