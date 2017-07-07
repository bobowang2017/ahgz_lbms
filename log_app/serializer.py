# -*- coding: utf-8 -*-
from rest_framework import serializers
from models import Log
from django.conf.global_settings import DATETIME_INPUT_FORMATS


class LogSerializer(serializers.ModelSerializer):

    operate_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',
                                             input_formats=DATETIME_INPUT_FORMATS,
                                             required=False)

    class Meta:
        model = Log
        fields = serializers.ALL_FIELDS
