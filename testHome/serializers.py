from django.contrib.auth.models import User, Group
from rest_framework import serializers
from testHome.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.CharField(required=True, min_length=6, allow_blank=False,
                                 error_messages={
                                     'required': '请填写姓名',
                                     'min_length': '名字不能小于6个字符'
                                 })
    psw = serializers.CharField(min_length=6)
    department = serializers.CharField(min_length=6)

    class Meta:
        model = UserInfo
        fields = ('user', 'psw', 'department')