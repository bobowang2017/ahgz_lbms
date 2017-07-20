# -*- coding: utf-8 -*-
from common_app.process import execute_sql


def get_permission_by_role(role_id):
    sql = "select a.view_id, a.parent_view_id, a.view_name, a.view_url, a.extra, b.view_option from " \
          "view a, role_mapping_view b where b.view_id = a.view_id and b.role_id=%s"
    params = [role_id]
    return execute_sql(sql, params)


def get_all_permission():
    sql = "select view_id, parent_view_id, view_name, view_url, extra, view_option from view"
    return execute_sql(sql, [])
