from django.db import models
from datetime import datetime

from users.models import UserProfile

from DjangoUeditor.models import UEditorField

# Create your models here.


class TaskModel(models.Model):
    title = models.CharField(max_length=100, default='', verbose_name='任务标题')
    task_man = models.ForeignKey(UserProfile, verbose_name='任务执行人')
    state = models.CharField(max_length=30, default='not', choices=(('accept', '已接受,正在进行中...'), ('done', '已完成'),
                                                                    ('not', '已下发')), null=True, blank=True,
                             verbose_name='任务状态')
    urgent = models.CharField(max_length=30, choices=(('ordinary', '普通'), ('worry', '紧急'),
                                                      ('must', '非常紧急')), null=True, blank=True,
                              verbose_name='紧急程度')
    content = UEditorField(default='', imagePath='task/task/', filePath='task/task/',
                           width=1000, height=300, verbose_name='任务内容')
    file = models.FileField(upload_to="task/file/", verbose_name="上传的文件")
    done_time = models.CharField(max_length=100, default='', verbose_name='规定完成时间')
    time = models.CharField(max_length=200, default='', verbose_name='任务处理时间')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '任务'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ApplyTaskModel(models.Model):
    task = models.ForeignKey(TaskModel, verbose_name='任务')
    # task_man = models.ForeignKey(UserProfile, verbose_name='申请人')
    cause = models.TextField(default='', verbose_name='延期原因')
    time = models.CharField(max_length=200, default='', verbose_name='延期到')
    state = models.CharField(max_length=30, default='submit', choices=(('agree', '同意'), ('not', '不同意'),
                                                                       ('submit', '已提交')), null=True, blank=True,
                             verbose_name='批复状态')
    leader = models.ForeignKey(UserProfile, verbose_name='批复人')
    detail = models.TextField(default='', verbose_name='详细意见')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '申请相关'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.task.title