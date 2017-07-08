# -*- coding: utf-8 -*-
from serializer import LogSerializer
from common_app.decorator import filter_none_param
from models import Log


def log_to_db(**kwargs):
    """
    记录日志到数据库中
    :return:
    """
    serializer = LogSerializer(data=kwargs)
    if serializer.is_valid(raise_exception=True):
        serializer.save()


@filter_none_param
def get_log_db(**kwargs):
    result = Log.objects.filter(**kwargs).order_by('-operate_time')
    return LogSerializer(result, many=True).data
