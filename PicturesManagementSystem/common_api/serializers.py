# 自己新建的对 token 和 user 的序列化
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class TokenSerializer(serializers.ModelSerializer):
    """
    用户信息序列化
    """
    first_name = serializers.CharField(source="user.username")
    last_name = serializers.CharField(source="user.username")
    phone = serializers.CharField(source="user.user.phone")
    email = serializers.CharField(source="user.email")
    date_joined = serializers.CharField(source="user.date_joined")
    uid = serializers.IntegerField(source="user.id")
    user_name=serializers.CharField(source="user.username")




    class Meta:
        model = Token
        fields = ('uid','user_name','first_name', 'last_name','phone',  'email', 'key', 'date_joined')   #

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name')