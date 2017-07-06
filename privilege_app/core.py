# -*- coding: utf-8 -*-
from django.db import connection


def get_permission_by_role(role_id):
    cursor = connection.cursor()
    cursor.execute(
        "select a.view_id, a.parent_view_id, a.view_name, a.view_url, a.extra from "
        "view a, role_mapping_view b where b.view_id = a.view_id and b.role_id=%s",
        [role_id]
    )
    result = cursor.fetchall()
    return list(result)
