# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-17 04:47
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', models.CharField(max_length=500, verbose_name='内容')),
                ('file', models.FileField(upload_to='file/%Y/%m', verbose_name='附件')),
                ('is_examine', models.CharField(blank=True, choices=[('adopt', '通过'), ('not', '未通过'), ('other', '审批中')], default='other', max_length=20, null=True, verbose_name='审批状态')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('nick_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='申请人')),
            ],
            options={
                'verbose_name': '审批事件',
                'verbose_name_plural': '审批事件',
            },
        ),
    ]
