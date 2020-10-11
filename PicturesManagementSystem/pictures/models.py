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





    class Meta:
        verbose_name = '图片'
        verbose_name_plural = '图片'
