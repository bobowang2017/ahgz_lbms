# -*- coding: utf-8 -*-
from rest_framework import serializers
from user_app.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = serializers.ALL_FIELDS
