# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class View(models.Model):
    view_id = models.IntegerField(verbose_name=u'视图编号', primary_key=True)
    parent_view_id = models.IntegerField(verbose_name=u'父级编号')
    view_url = models.CharField(max_length=128, verbose_name=u'URL导航地址')
    view_name = models.CharField(max_length=32, verbose_name=u'URL导航名称')
    extra = models.CharField(max_length=128, verbose_name=u'备注信息', null=True)

    class Meta:
        verbose_name = u'视图表'
        verbose_name_plural = verbose_name
        db_table = 'view'

    def __unicode__(self):
        return self


class Role(models.Model):
    role_id = models.IntegerField(max_length=5, verbose_name=u'角色编号', primary_key=True)
    role_name = models.CharField(max_length=32, verbose_name=u'角色名称')
    extra = models.CharField(max_length=128, verbose_name=u'备注信息', null=True)

    class Meta:
        verbose_name = u'角色表'
        verbose_name_plural = verbose_name
        db_table = 'role'

    def __unicode__(self):
        return self


class RoleMappingView(models.Model):
    id = models.AutoField(verbose_name=u'序列号', primary_key=True)
    role_id = models.IntegerField(verbose_name=u'角色编号')
    view_id = models.CharField(max_length=32, verbose_name=u'视图编号')

    class Meta:
        verbose_name = u'角色视图关系表'
        verbose_name_plural = verbose_name
        db_table = 'role_mapping_view'

    def __unicode__(self):
        return self
