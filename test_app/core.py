# -*- coding: utf-8 -*-
import traceback
import urllib

from common_app.decorator import filter_none_param
from serializer import UserSerializer
from models import User
import json
from django.db import transaction
import urllib2


@filter_none_param
def create_user(**kwargs):
    serializer = UserSerializer(data=kwargs)
    if serializer.is_valid(raise_exception=True):
        serializer.save(**kwargs)


@filter_none_param
def get_user(page_num, page_size, **kwargs):
    start = (page_num - 1) * page_size
    end = start + page_size
    result = User.objects
    if kwargs.get('user_number'):
        user_number = kwargs.get('user_number')
        kwargs.pop('user_number')
        result = result.filter(user_number__contains=user_number)
    if kwargs.get('user_name'):
        user_name = kwargs.get('user_name')
        kwargs.pop('user_name')
        result = result.filter(user_name__contains=user_name)
    if kwargs.get('user_phone'):
        user_phone = kwargs.get('user_phone')
        kwargs.pop('user_phone')
        result = result.filter(user_phone__contains=user_phone)
    result = result.filter(**kwargs).order_by('user_number')[start: end]
    return UserSerializer(result, many=True).data


def check_password(user_id, user_password):
    user = User.objects.filter(user_id=user_id)
    if user.user_password == user_password:
        return True
    return False


@filter_none_param
def get_user_total(**kwargs):
    result = User.objects
    if kwargs.get('user_number'):
        user_number = kwargs.get('user_number')
        kwargs.pop('user_number')
        result = result.filter(user_number__contains=user_number)
    if kwargs.get('user_name'):
        user_name = kwargs.get('user_name')
        kwargs.pop('user_name')
        result = result.filter(user_name__contains=user_name)
    if kwargs.get('user_phone'):
        user_phone = kwargs.get('user_phone')
        kwargs.pop('user_phone')
        result = result.filter(user_phone__contains=user_phone)
    result = result.filter(**kwargs)
    return len(UserSerializer(result, many=True).data)


@transaction.atomic
def delete_users_by_ids(id_list):
    User.objects.filter(user_id__in=id_list).delete()


@filter_none_param
def update_user_by_id(user_id, **kwargs):
    User.objects.filter(user_id=user_id).update(**kwargs)


def get_tree_view(**kwargs):
    role_type = kwargs.get('user_role', 0)
    with open('collect_static/json/tree.json', 'r') as f:
        result = json.loads(f.read())
        return result['customer_tree'] if role_type == 0 else result['manager_tree']

