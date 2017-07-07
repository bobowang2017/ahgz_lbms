# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import traceback

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import socket
from common_app.process import response_data
from log_action_conf import ACTION_VALUE
from core import log_to_db, get_log_db


class LogTestView(APIView):

    def post(self, request):
        user_id = '123'
        user_name = 'zhangsan'
        ip = socket.gethostbyname(socket.gethostname())
        action = ACTION_VALUE.get('test')
        try:
            log_to_db(operate_user_id=user_id, operate_user_name=user_name, operate_action=action, operate_ip=ip)
        except Exception as e:
            traceback.print_exc()
            return Response(response_data(-2, 'exception', e), status=status.HTTP_200_OK)
        return Response(response_data(0, 'success', None), status=status.HTTP_200_OK)

    def get(self, request):
        try:
            result = get_log_db()
        except Exception as e:
            traceback.print_exc()
            return Response(response_data(-2, 'exception', e), status=status.HTTP_200_OK)
        return Response(response_data(0, 'success', result), status=status.HTTP_200_OK)
