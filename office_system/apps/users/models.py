from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, default='', verbose_name='姓名')
    mobile = models.CharField(max_length=11, default='', verbose_name='手机号码')
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), null=True,
                              blank=True, verbose_name='性别')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='邮箱')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '员工基本信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class DivisionModel(models.Model):
    name = models.CharField(max_length=10, default='', verbose_name='部门')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '部门信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserDetail(models.Model):
    user = models.ForeignKey(UserProfile, null=True, verbose_name='员工姓名')
    birthday = models.CharField(max_length=20, null=True, default='', verbose_name='出生日期')
    # education = models.CharField(max_length=20, null=True, default='', verbose_name='学历')
    education = models.CharField(max_length=20, choices=(('college', '大专'), ('undergraduate', '本科'),
                                                        ('graduate', '研究生'), ('doctor', '博士生')), default='undergraduate',
                                 verbose_name='学历')
    major = models.CharField(max_length=20, null=True, default='', verbose_name='专业')
    work_year = models.CharField(max_length=10, null=True, default='', verbose_name='工作年限')
    # policital_status = models.CharField(max_length=10, null=True, default='', verbose_name='政治面貌')
    policital_status = models.CharField(max_length=6, choices=(('party', '党员'), ('masses', '群众'), ('other', '其他')),
                                        default='masses', verbose_name='政治面貌')
    native_place = models.CharField(max_length=50, null=True, default='', verbose_name='籍贯')
    home_address = models.CharField(max_length=50, null=True, default='', verbose_name='家庭住址')
    permanent_address = models.CharField(max_length=11, null=True, default='', verbose_name='户口所在地')
    division = models.ForeignKey(DivisionModel, null=True, verbose_name='所属部门')
    position = models.CharField(max_length=20, null=True, default='', verbose_name='职位')
    work_num = models.IntegerField(null=True, default=0, verbose_name='工号')
    is_work = models.CharField(max_length=6, choices=(('job', '在职'), ('quit', '离职')), default='job',
                               verbose_name='是否在职')
    entry_time = models.CharField(max_length=20, null=True, default='', verbose_name='入职时间')
    entry_year = models.CharField(max_length=5, null=True, default='', verbose_name='本公司入职年限')
    telephone = models.CharField(max_length=12, null=True, default='', verbose_name='座机号码')
    email = models.EmailField(max_length=100, null=True, default='', verbose_name='公司邮箱')
    remarks = models.CharField(max_length=50, null=True, default='', verbose_name='备注')
    base_pay = models.FloatField(default=0, verbose_name='基本工资')
    post_wage = models.FloatField(default=0, verbose_name='岗位')
    bonus = models.FloatField(default=0, verbose_name='绩效奖金')
    benefits = models.FloatField(default=0, verbose_name='保险金(前端四金)')
    mobile_fee = models.FloatField(default=0, verbose_name='通讯费')
    car_fee = models.FloatField(default=0, verbose_name='车费')
    lunch_fee = models.FloatField(default=0, verbose_name='午餐费')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '员工详细信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.nick_name