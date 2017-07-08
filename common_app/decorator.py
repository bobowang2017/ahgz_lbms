# -*- coding: utf-8 -*-


# 去掉函数中参数值是None的参数
import functools


def filter_none_param(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        params = dict()
        for key in kwargs:
            if kwargs[key] is not None:
                params[key] = kwargs[key]
        return func(*args, **params)
    return _wrapper
