from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model

from users.models import UserProfile

User = get_user_model()



# Create your models here.


class ApplyModel(models.Model):
    title = models.CharField(max_length=50, null=False, verbose_name='标题')
    content = models.TextField(null=False, verbose_name='内容')
    is_examine = models.CharField(max_length=20, choices=(('adopt', '通过'), ('not', '未通过'), ('other', '审批中')),
                                  null=True, blank=True, default='other', verbose_name='审批状态')
    file = models.FileField(max_length=50, upload_to='file/%Y/%m', verbose_name='附件')
    nick_name = models.ForeignKey(UserProfile, null=True, verbose_name='申请人')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '审批事件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title