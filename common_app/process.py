# -*- coding: utf-8 -*-
import json


def response_data(ret_code, message, data):
    result = {'ret_code': ret_code, 'message': message, 'data': data}
    return json.dumps(result, ensure_ascii=False)