from django.shortcuts import render

# Create your views here.
from rest_framework.test import APIRequestFactory
from rest_framework.request import Request
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from testHome.serializers import *
from testHome.models import *
from rest_framework.response import Response
from rest_framework import status
from common.common import *

from rest_framework import generics


def format_error_message(error):
    error_list = list(error.detail.values())
    messages = [
        '; '.join([_(error) for error in errors])
        for errors in error_list
    ]
    error_type = type(error)
    raise error_type(detail={_('message'): '; '.join(messages)})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserInfoViewSet(viewsets.ModelViewSet):
    # queryset - 用于从视图返回对象的查询结果集。通常，你必须设置此属性或者重写 get_queryset() 方法。如果你重写了一个视图的方法，
    # 重要的是你应该调用 get_queryset() 方法而不是直接访问该属性，因为 queryset 将被计算一次，这些结果将为后续请求缓存起来
    queryset = UserInfo.objects.all()
    # serializer_class - 用于验证和反序列化输入以及用于序列化输出的Serializer类。 通常，你必须设置此属性或者重写get_serializer_class() 方法
    serializer_class = UserInfoSerializer

    # def list(self, request, *args, **kwargs):
    #     queryset = UserInfo.objects.all()
    #     serializer = UserInfoSerializer(queryset, many=True)
    #     return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        queryset = UserInfo.objects.filter(user=request.data['user'])
        serializer = UserInfoSerializer(data=request.data)
        if len(queryset) >= 1:
            return JsonResponse(code=200, data=[], msg="用户已经存在")
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print(headers)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return JsonResponse(code=200, data=[], msg="注册成功")

    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = UserInfo
    #     print("进入这里")
    #     serializer = UserInfoSerializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     print("进入这里2222")
    #     self.perform_update(serializer)
    #     # if getattr(instance, '_prefetched_objects_cache', None):
    #     #     # If 'prefetch_related' has been applied to a queryset, we need to
    #     #     # forcibly invalidate the prefetch cache on the instance.
    #     #     instance._prefetched_objects_cache = {}
    #
    #     return JsonResponse(code=200, data=[''], msg="更新成功")

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


#
# class RegisteredViewSet(viewsets.ModelViewSet):
#     queryset = UserInfo.objects.all()
#     serializer_class = RegisteredSerializer
#
#     def create(self, request, *args, **kwargs):
#         queryset = UserInfo.objects.all()
#         print(request.data['user'])
#         if request.data['user'] in queryset:
#             pass
#         serializer = RegisteredSerializer(data=request.data, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response("注册成功")


# class UserInfoViewSet(generics.ListCreateAPIView):
#     queryset = UserInfo.objects.all()
#     serializer_class = UserInfoSerializer

# 登录接口
class LoginViewSet(viewsets.ModelViewSet):
    serializer_class = UserInfoSerializer


# 项目
class ProjectInfoViewSet(viewsets.ModelViewSet):
    queryset = ProjectInfo.objects.all()
    serializer_class = ProjectInfoSerializer


# 基础配置
class ConfigInfoViewSet(viewsets.ModelViewSet):
    queryset = ConfigInfo.objects.all()
    serializer_class = ConfigInfoSerializer


# 模块
class ModelsInfoViewSet(viewsets.ModelViewSet):
    queryset = ModelsInfo.objects.all()
    serializer_class = ModelsInfoSerializer

    def list(self, request, *args, **kwargs):
        queryset = ModelsInfo.objects.all()
        serializer = ModelsInfoSerializer(queryset, many=True)
        return JsonResponse(code=status.HTTP_200_OK, data=[serializer.data], msg="成功")

    def create(self, request, *args, **kwargs):
        serializer = ModelsInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# 测试用例编写
class CaseInfoViewSet(viewsets.ModelViewSet):
    queryset = CaseInfo.objects.all()
    serializer_class = CaseInfoSerializer
