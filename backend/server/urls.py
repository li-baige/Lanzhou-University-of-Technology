"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from App.views import confirmed, index
from App import views as App_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    # 用户user请求匹配数据
    path('api/boundary', App_view.boundary),             # 小区边界坐标
    path('api/village_name',App_view.village_name),      # 小区名字
    path('api/confirm', App_view.confirm),               # 累计确诊
    path('api/village_data', App_view.village_data),     # 小区接口
    path('api/confirmed', App_view.confirmed),           # 确诊病历号信息
    path('api/city', App_view.city),                     # 城市疫情具体信息
    path('api/village_date', App_view.village_date),     # 小区信息
    path('api/community_name', App_view.community_name), # 小区确诊人员信息
]
