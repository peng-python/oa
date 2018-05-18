from django.db import models
from datetime import datetime

from DjangoUeditor.models import UEditorField
from users.models import UserProfile

# Create your models here.


class CategoryModel(models.Model):
    name = models.CharField(max_length=50, default='', verbose_name='名称')
    subject = models.CharField(max_length=200, default='', verbose_name='类别备注')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '公告类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class NoticeModel(models.Model):
    title = models.CharField(max_length=50, null=False, verbose_name='标题')
    subject = models.CharField(max_length=500, null=False, verbose_name='主题')
    content = UEditorField(default='', imagePath='notice/content/', filePath='notice/content/',
                           width=1000, height=300, verbose_name='公告内容')
    author = models.ForeignKey(UserProfile, verbose_name='发布人')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '公告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title