# -*- coding:utf-8 -*-

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from pictures.models import Image



class ImageSerializer(serializers.ModelSerializer):
    """
    项目信息序列化
    """
    class Meta:
        model = Image
        fields = ('id', 'title', 'original',"uid_id")




