"""IplatForm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from testHome import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'userInfo', views.UserInfoViewSet)
router.register(r'projectInfo', views.ProjectInfoViewSet)
router.register(r'configInfo', views.ConfigInfoViewSet)
router.register(r'modelsInfo', views.ModelsInfoViewSet)
router.register(r'caseInfo', views.CaseInfoViewSet)
# router.register(r'runCase', views.getlispic)
# router.register(r'Registered', views.RegisteredViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('run/', views.RunCaseViewSet)
]
