# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-17 16:22
from __future__ import unicode_literals

import DjangoUeditor.models
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
            name='ApplyTaskModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause', models.TextField(default='', verbose_name='延期原因')),
                ('time', models.CharField(default='', max_length=200, verbose_name='延期到')),
                ('state', models.CharField(blank=True, choices=[('agree', '同意'), ('not', '不同意'), ('submit', '已提交')], max_length=30, null=True, verbose_name='批复状态')),
                ('detail', models.TextField(default='', verbose_name='详细意见')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='批复人')),
            ],
            options={
                'verbose_name': '申请相关',
                'verbose_name_plural': '申请相关',
            },
        ),
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='任务标题')),
                ('state', models.CharField(blank=True, choices=[('accept', '已接受,正在进行中...'), ('done', '已完成'), ('not', '已下发')], max_length=30, null=True, verbose_name='任务状态')),
                ('urgent', models.CharField(blank=True, choices=[('ordinary', '普通'), ('worry', '紧急'), ('must', '非常紧急')], max_length=30, null=True, verbose_name='紧急程度')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='任务内容')),
                ('file', models.FileField(upload_to='task/file/', verbose_name='上传的文件')),
                ('time', models.CharField(default='', max_length=200, verbose_name='任务处理时间')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('task_man', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='任务执行人')),
            ],
            options={
                'verbose_name': '任务',
                'verbose_name_plural': '任务',
            },
        ),
        migrations.AddField(
            model_name='applytaskmodel',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.TaskModel', verbose_name='任务'),
        ),
    ]