from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Image(models.Model):
    # title = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250, blank=True)
    original = models.ImageField(upload_to=settings.IMAGE_PREFIX)
    created = models.DateTimeField(auto_now_add=True)
    uid = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    type=models.CharField(max_length=30, blank=True,default=1)
    width= models.IntegerField(verbose_name='图片宽度',default=1)
    height= models.IntegerField( verbose_name='图片高度',default=1)
    size=models.IntegerField(verbose_name='图片大小',default=1)
    auto_tag = models.ForeignKey("Auto_Tag",on_delete=models.CASCADE,default=1)
    location_tag= models.ForeignKey("Location_Tag",on_delete=models.CASCADE,default=1)



    class Meta:
        verbose_name = '图片'
        verbose_name_plural = '图片'


class Auto_Tag(models.Model):
    auto_tag_name=models.CharField(max_length=30, verbose_name='自动分类')



class Location_Tag(models.Model):
    location_tag_name=models.CharField(max_length=30, verbose_name='地标分类')



