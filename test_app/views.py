# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from common_app.process import response_data
from core import create_user, get_user, get_tree_view, get_user_total, delete_users_by_ids, update_user_by_id, check_password
import uuid, logging, random


class TestUserView(APIView):

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
        user_phone = query_params.get('user_phone', None)
        user_phone = None if str(user_phone) == '' else user_phone
        user_status = query_params.get('user_status', None)
        try:
            user_list = get_user(page_num, page_size, user_number=user_number, user_email=user_email,
                                 user_phone=user_phone, user_status=user_status, user_name=user_name)
            user_total = get_user_total(user_number=user_number, user_email=user_email,
                                        user_phone=user_phone, user_status=user_status, user_name=user_name)
            data = dict()
            data['rows'] = user_list
            data['total'] = user_total
        except Exception as e:
            traceback.print_exc()
            return Response(response_data(-2, 'exception', e), status=status.HTTP_200_OK)
        return Response(response_data(0, 'success', data), status=status.HTTP_200_OK)

    def post(self, request):
        user_id = str(uuid.uuid5(uuid.uuid4(), str(uuid.uuid4())))
        user_number = random.randint(10000, 20000)
        user_name = str(request.data.get('user_name')).strip()
        user_sex = True if request.data.get('user_sex') == 0 else False
        user_birthday = request.data.get('user_birthday')
        user_email = str(request.data.get('user_email')).strip()
        user_phone = str(request.data.get('user_phone')).strip()
        user_address = request.data.get('user_address')
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
                        user_address=user_address,user_password=user_number)
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
        user_address = query_params.get('user_address')
        user_password = query_params.get('user_password')
        if user_id is None:
            return Response(response_data(-1, 'error', 'Param user_id is None'), status=status.HTTP_200_OK)
        try:
            update_user_by_id(user_id, user_name=user_name, user_sex=user_sex, user_email=user_email,
                              user_phone=user_phone, user_address=user_address, user_password=user_password)
        except Exception as e:
            traceback.print_exc()
            return Response(response_data(-2, 'exception', e), status=status.HTTP_200_OK)
        return Response(response_data(0, 'success', None), status=status.HTTP_200_OK)


class AuthView(APIView):

    def post(self, request):
        data = request.data
        user_id = data.get('user_id')
        user_password = data.get('user_password')
        if user_id is None or user_password is None:
            return Response(response_data(-1, 'error', 'Param user_id or user_password is None'), status=status.HTTP_200_OK)
        try:
            result = check_password(user_id=str(user_id), user_password=str(user_password))
            if result is False:
                raise Exception(u'用户名密码不匹配')
            # 认真成功之后请求授权码
            sche = request.scheme
            host = request.get_host()
            redirect_url = sche + '://' + host
        except Exception as e:
            traceback.print_exc()
            return Response(response_data(-2, 'exception', e), status=status.HTTP_200_OK)
        return Response(response_data(0, 'success', result), status=status.HTTP_200_OK)


class RoleUrlView(APIView):

    def get(self, request):
        user_role = request.query_params.get('user_role', 0)
        try:
            result = get_tree_view(user_role=user_role)
        except Exception as e:
            traceback.print_exc()
            logging.exception('RoleUrlView -> 获取导航树失败')
            return Response(response_data(-2, 'exception', u'获取导航树失败'), status=status.HTTP_200_OK)
        return Response(response_data(0, 'success', result), status=status.HTTP_200_OK)


class TestUserView(APIView):

    def get(self, request):
        try:
            for i in range(10, 15):
                user_id = str(uuid.uuid5(uuid.uuid4(), str(uuid.uuid4())))
                user_name = 'zhang' + str(i)
                user_sex = True
                user_birthday = '1989-08-15'
                user_email = '283803150@qq.com'
                user_phone = '15926547569'
                user_address = 'wuhan'
                user_number = i

                create_user(user_id=user_id, user_name=user_name, user_sex=user_sex, user_birthday=user_birthday,
                            user_email=user_email, user_phone=user_phone, user_address=user_address,
                            user_number=user_number)
        except Exception as e:
            traceback.print_exc()
            return Response(response_data(-2, 'exception', u'获取导航树失败'), status=status.HTTP_200_OK)
        return Response(response_data(0, 'success', None), status=status.HTTP_200_OK)
