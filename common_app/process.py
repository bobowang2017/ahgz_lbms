# -*- coding: utf-8 -*-
import json
from django.db import connection


def response_data(ret_code, message, data):
    result = {'ret_code': ret_code, 'message': message, 'data': data}
    return json.dumps(result, ensure_ascii=False)


def execute_sql(sql, params):
    if not isinstance(params, list):
        raise Exception(u'Execute sql exception: params is not list')
    cursor = connection.cursor()
    cursor.execute(sql, params)
    result = cursor.fetchall()
    return list(result)
