# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import traceback
import uuid
import time
# Create your views here.
import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from common_app.process import response_data
from user_app.core import get_user, create_user, delete_users_by_ids, update_user_by_id


class UserView(APIView):

    def get(self, request):
        query_params = request.query_params
        page_num = int(query_params.get('page', 1))
        page_size = int(query_params.get('rows', 10))
        user_number = query_params.get('user_number', None)
        user_number = None if str(user_number) == '' else user_number
        user_name = query_params.get('user_name', None)
        user_name = None if str(user_name) == '' else user_name
        user_email = query_params.get('user_email', None)
        user_email = None if str(user_email) == '' else user_email
        department_id = query_params.get('department_id', None)
        department_id = None if str(department_id) == '' else department_id
        user_phone = query_params.get('user_phone', None)
        user_phone = None if str(user_phone) == '' else user_phone
        user_status = query_params.get('user_status', None)
        try:
            user_list = get_user(page_num, page_size, user_number=user_number, user_email=user_email,
                                 user_phone=user_phone, user_status=user_status, user_name=user_name,
                                 department_id=department_id)
            data = dict()
            data['rows'] = user_list
        except Exception as e:
            traceback.print_exc()
            return Response(response_data(-2, 'exception', e), status=status.HTTP_200_OK)
        return Response(response_data(0, 'success', data), status=status.HTTP_200_OK)

    def post(self, request):
        user_id = str(uuid.uuid5(uuid.uuid4(), str(uuid.uuid4())))
        user_number = random.randint(10000, 20000)
        user_name = str(request.data.get('user_name')).strip()
        user_sex = True if request.data.get('user_sex') == 0 else False
        user_birthday = str(request.data.get('user_birthday'))
        user_birthday = datetime.datetime.strptime(user_birthday, '%Y-%m-%d %H:%M:%S')
        user_email = str(request.data.get('user_email')).strip()
        user_phone = str(request.data.get('user_phone')).strip()
        user_address = request.data.get('user_address')
        department_id = request.data.get('department_id')
        if user_address is not None:
            user_address = str(user_address)
        error_msg = None
        if user_name is None:
            error_msg = 'Param user_name is None'
        if user_birthday is None:
            error_msg = 'Param user_birthday is None'
        if user_email is None:
            error_msg = 'Param user_email is None'
        if user_phone is None:
            error_msg = 'Param user_phone is None'
        if error_msg is not None:
            return Response(response_data(-1, 'error', error_msg), status=status.HTTP_200_OK)
        try:
            create_user(user_id=user_id, user_number=user_number, user_name=user_name, user_sex=user_sex,
                        user_birthday=user_birthday, user_email=user_email, user_phone=user_phone,
                        user_address=user_address, user_password=user_number, department_id=department_id)
        except Exception as e:
            traceback.print_exc()
            return Response(response_data(-2, 'exception', e), status=status.HTTP_200_OK)
        return Response(response_data(0, 'success', None), status=status.HTTP_200_OK)

    def delete(self, request):
        query_params = request.data
        ids = query_params.get('ids', None)
        if ids is None or str(ids) == '' or len(str(ids).split(',')) == 0:
            return Response(response_data(-1, 'error', 'Param is None'), status=status.HTTP_200_OK)
        id_list = str(ids).split(',')
        try:
            delete_users_by_ids(id_list)
        except Exception as e:
            traceback.print_exc()
            return Response(response_data(-2, 'exception', e), status=status.HTTP_200_OK)
        return Response(response_data(0, 'success', None), status=status.HTTP_200_OK)


    def put(self, request):
        query_params = request.data
        user_id = query_params.get('user_id')
        user_name = query_params.get('user_name')
        user_sex = query_params.get('user_sex')
        user_email = query_params.get('user_email')
        user_phone = query_params.get('user_phone')
        department_id = query_params.get('department_id')
        user_address = query_params.get('user_address')
        user_password = query_params.get('user_password')
        if user_id is None:
            return Response(response_data(-1, 'error', 'Param user_id is None'), status=status.HTTP_200_OK)
        try:
            update_user_by_id(user_id, user_name=user_name, user_sex=user_sex, user_email=user_email,
                              user_phone=user_phone, user_address=user_address, department_id=department_id,
                              user_password=user_password)
        except Exception as e:
            traceback.print_exc()
            return Response(response_data(-2, 'exception', e), status=status.HTTP_200_OK)
        return Response(response_data(0, 'success', None), status=status.HTTP_200_OK)
