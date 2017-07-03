# -*- coding: utf-8 -*-
from rest_framework import serializers
from test_app.models import User
from django.conf.global_settings import DATETIME_INPUT_FORMATS


class UserSerializer(serializers.ModelSerializer):
    role_type = (
        (0, 'customer'),
        (1, 'manager'),
    )
    user_status = (
        (0, '正常状态'),
        (-1, '禁用状态'),
        (-2, '过期'),
    )
    user_id = serializers.CharField(max_length=64)
    user_name = serializers.CharField(allow_blank=False, max_length=64)
    user_number = serializers.CharField(allow_blank=False, max_length=10)
    user_sex = serializers.BooleanField(default=True)
    user_birthday = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',
                                              input_formats=DATETIME_INPUT_FORMATS,
                                              required=False)
    user_email = serializers.CharField(max_length=64)
    user_phone = serializers.CharField(max_length=11)
    user_address = serializers.CharField(max_length=256, default=0, allow_null=True)
    user_password = serializers.CharField(max_length=256, default=0, allow_null=True)
    user_role = serializers.ChoiceField(choices=role_type, default=0)
    register_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',
                                              input_formats=DATETIME_INPUT_FORMATS,
                                              required=False)
    user_status = serializers.ChoiceField(choices=user_status, default=0)

    class Meta:
        model = User
        fields = serializers.ALL_FIELDS

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, user, validated_data):
        user.user_id = validated_data.get('user_id', user.user_id)
        user.user_name = validated_data.get('user_name', user.user_name)
        user.user_number = validated_data.get('user_number', user.user_number)
        user.user_sex = validated_data.get('user_sex', user.user_sex)
        user.user_birthday = validated_data.get('user_birthday', user.user_birthday)
        user.user_email = validated_data.get('user_email', user.user_email)
        user.user_phone = validated_data.get('user_phone', user.user_phone)
        user.user_address = validated_data.get('user_address', user.user_address)
        user.user_role = validated_data.get('user_role', user.user_role)
        user.register_time = validated_data.get('register_time', user.register_time)
        user.user_status = validated_data.get('user_status', user.user_status)
        user.save()
        return user
