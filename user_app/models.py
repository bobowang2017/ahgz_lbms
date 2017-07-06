# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    user_status = (
        (0, u'正常状态'),
        (-1, u'禁用状态'),
        (-2, u'过期'),
    )
    user_id = models.CharField(max_length=64, verbose_name=u'序号', primary_key=True)
    user_number = models.CharField(max_length=10, verbose_name=u'编号', unique=True)
    user_name = models.CharField(max_length=64, verbose_name=u'姓名')
    user_sex = models.BooleanField(default=True, verbose_name=u'性别')
    user_birthday = models.DateTimeField(verbose_name=u'出生日期')
    user_email = models.CharField(max_length=64, verbose_name=u'邮箱')
    user_phone = models.CharField(max_length=11, verbose_name=u'手机号码')
    user_address = models.CharField(max_length=256, verbose_name=u'家庭住址', default=0)
    user_password = models.CharField(max_length=256, verbose_name=u'用户密码', null=True)
    department_id = models.CharField(max_length=64, verbose_name=u'部门ID')
    register_time = models.DateTimeField(auto_now_add=True, verbose_name=u'注册时间')
    user_status = models.IntegerField(choices=user_status, verbose_name=u'状态',  default=0)

    class Meta:
        verbose_name = u'用户表'
        verbose_name_plural = verbose_name
        db_table = 'user'

    def __unicode__(self):
        return self
