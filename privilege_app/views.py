# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from core import get_permission_by_role
from common_app.process import response_data


class PrivilegeView(APIView):

    def get(self, request):
        role_id = request.query_params.get('role_id', None)
        if role_id is None:
            return Response(response_data(0, 'ParamError', 'Param role_id is None'), status=status.HTTP_200_OK)
        result = get_permission_by_role(role_id)
        return Response(response_data(0, 'Success', result), status=status.HTTP_200_OK)
