# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from core import get_permission_by_role, get_all_permission
from common_app.process import response_data


class PrivilegeView(APIView):

    def get(self, request):
        """
        通过用户角色获取到该角色对应的系统导航栏目
        :param request:  role_id
        :return:
        """
        role_id = request.query_params.get('role_id', None)
        try:
            if role_id:
                result = get_permission_by_role(role_id)
            else:
                result = get_all_permission()
        except Exception as e:
            return Response(response_data(0, 'Exception', e), status=status.HTTP_200_OK)
        result_wrapper = self.wrapper_result_json(result, result[0])
        return Response(response_data(0, 'Success', result_wrapper), status=status.HTTP_200_OK)

    def wrapper_result_json(self, results, opt_obj):
        """
        将查询到的导航列表包装成json数据格式
        :param results:
        :param opt_obj:
        :return:
        """
        id = opt_obj[0]
        children = list()
        for result in results:
            if result[1] == id:
                child = self.wrapper_result_json(results, result)
                children.append(child)
        opt_result = dict()
        opt_result["url"] = opt_obj[3]
        opt_result["url_name"] = opt_obj[2]
        opt_result["option"] = opt_obj[5]
        if children:
            opt_result["children"] = children
        return opt_result

