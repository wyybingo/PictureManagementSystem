from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView   # 新增1

from .api import user

urlpatterns = [
    url(r'user/login', user.ObtainAuthToken.as_view()),   #

]
