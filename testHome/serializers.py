from django.contrib.auth.models import User, Group
from rest_framework import serializers
from testHome.models import *
from common.common import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


# 序列化器序列化器是一个位于客户端和后台之间的中间层。这个中间层一个最基本的作用就是接受前端JSON字符串转化为后台python可以识别的对象；
# 从后台获取python对象然后转化为给前端的JSON格式字符串
class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.CharField(required=True, min_length=6, allow_blank=False,
                                 error_messages={
                                     'required': '请填写姓名',
                                     'min_length': '名字不能小于6个字符'
                                 })
    psw = serializers.CharField(min_length=6)
    department = serializers.CharField(min_length=6)

    def user_valid(self, value):
        if value:
            pass

    class Meta:
        model = UserInfo
        fields = ('user', 'psw', 'department')


class ProjectInfoSerializer(serializers.HyperlinkedModelSerializer):
    project_name = serializers.CharField(max_length=50)
    responsible_name = serializers.CharField(max_length=20)
    test_user = serializers.CharField(max_length=100)
    dev_user = serializers.CharField(max_length=100)
    publish_app = serializers.CharField(max_length=60,
                                        error_messages={
                                            "max_length": "不能超过60字符"
                                        })
    simple_desc = serializers.CharField(max_length=500,
                                        error_messages={
                                            "max_length": "不能超过500字符"
                                        })
    other_desc = serializers.CharField(max_length=100,
                                       error_messages={
                                           "max_length": "不能超过100字符"
                                       })
    status = serializers.IntegerField(min_value=0,
                                      error_messages={})

    # def create(self, validated_data):

    class Meta:
        model = ProjectInfo
        fields = ('project_name', 'responsible_name', 'test_user', 'dev_user', 'publish_app', 'simple_desc',
                  'simple_desc', 'other_desc', 'status')


class ConfigInfoSerializer(serializers.HyperlinkedModelSerializer):
    status = serializers.CharField(max_length=50)

    class Meta:
        model = ConfigInfo
        fields = '__all__'


class ModelsInfoSerializer(serializers.HyperlinkedModelSerializer):
    # belong_project = ProjectInfoSerializer()
    status_id = serializers.CharField()
    belong_project_id = serializers.CharField()
    models_name = serializers.CharField(max_length=1,
                                        error_messages={
                                            "max_length": "字数不能超过50字符"
                                        })
    models_desc = serializers.CharField(max_length=50,
                                        error_messages={
                                            "max_length": "字数不能超过50字符"
                                        })
    other_desc = serializers.CharField(max_length=100,
                                       error_messages={
                                           "max_length": "字数不能超过100字符"
                                       })

    class Meta:
        model = ModelsInfo
        fields = ('status_id', 'belong_project_id', 'models_name', 'models_desc', 'other_desc')


class CaseInfoSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    belong_project = serializers.CharField(max_length=50)
    include = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=20)
    request = models.TextField()
    status = serializers.IntegerField()

    # objects = TestCaseInfoManager()
    class Meta:
        model = CaseInfo
        fields = ('type', 'name', 'belong_project', 'belong_module_id', 'include', 'author', 'request', 'status')

# class VerifyForm(serializers.Serializer):
#     """验证认证用户输入数据"""
#     username = serializers.CharField(max_length=64, min_length=2)
#     id_number = serializers.CharField(max_length=18, min_length=15)
#     sms_code = serializers.CharField(max_length=6, min_length=6)
#
#     def validate_username(self, value):
#         if 检测输入的用户名不合法:
#             raise 异常
#         return value
#
#     def validate_id_number(self, value):
#         if 检测输入的身份证号码不合法:
#             raise 异常
#         return value
#
#     def validate_sms_code(self, value):
#         if 检测输入的短信验证码不合法:
#             raise 异常
#         return value
#
#     def validate(self, attrs):
#         if 外部服务(username, id_number) 不合法:
#             raise 异常
#         return attrs
#
#     def create(self, validated_data):
#         持久化
#         return instance
