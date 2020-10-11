# _*_ coding:utf-8 _*_


from django.conf.urls import url

from .views import *



urlpatterns = [
    url(r'uploadImg', upload_img.as_view()),
    url(r'getImage', getImage.as_view()),
    url(r'searchImage', getImage.as_view()),

]
