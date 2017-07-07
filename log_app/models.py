# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Log(models.Model):

    id = models.AutoField(verbose_name=u'序号', primary_key=True)
    operate_user_id = models.CharField(max_length=64, verbose_name=u'操作人编号')
    operate_user_name = models.CharField(max_length=64, verbose_name=u'操作人姓名')
    operate_time = models.DateTimeField(auto_now=True, verbose_name='操作时间', null=True)
    operate_action = models.CharField(max_length=128, verbose_name='操作行为')
    operate_ip = models.CharField(max_length=32, verbose_name='操作人IP地址')

    class Meta:
        verbose_name = u'日志表'
        verbose_name_plural = verbose_name
        db_table = 'log'

    def __unicode__(self):
        return self



