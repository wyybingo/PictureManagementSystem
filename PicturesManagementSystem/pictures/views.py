from django.shortcuts import render
from rest_framework.views import APIView
from common_api.api.api_response import JsonResponse
from .models import Image
import os
from pictures.serializers import ImageSerializer


# Create your views here.

class upload_img(APIView):

    cur_path = os.path.dirname(os.path.realpath(__file__))

    def post(self, request):
        uid_id=request.POST.get("uid")
        img_files = request.FILES.getlist("file")
        repeat_img = []
        for img in img_files:
            upload_dir = os.path.join(self.cur_path, "uploads")
            file_path = os.path.join(upload_dir, img.name)
            pic_name = os.path.basename(file_path)

            #
            # # 获取当前目录的上一级
            # root_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
            # save_dir = os.path.join(root_path,"uploads")
            # print(upload_dir)
            # # 存储图片到uploads文件夹
            # save_path = os.path.join(save_dir, img.name)
            # print(file_path)

            if os.path.exists(file_path):
                repeat_img.append(img.name)
            else:
                images = Image(original=img,uid_id=uid_id,
                               title = pic_name
                               )
                images.save()
        if len(repeat_img) == len(img_files):
            return JsonResponse(code="999998", msg="上传失败,所有文件均重复")
        elif not repeat_img:
            return JsonResponse(code="999999", msg="所有文件上传成功")
        else:
            return JsonResponse(code="999996", msg="上传成功,存在重复文件", data={"repeat_file": repeat_img})






class getImage(APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = ()

    def get(self, request):
        """
        获取图片
        :param request:
        :return:
        """
        uid_id=request.GET.get("uid")
        obj = Image.objects.filter(uid_id=uid_id).order_by("id")

        serialize = ImageSerializer(obj, many=True)
        return JsonResponse(data={"data": serialize.data,
                                  }, code="999999", msg="搜索成功")




class searchImage(APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = ()

    def get(self, request):
        """
        获取图片
        :param request:
        :return:
        """
        uid_id=request.GET.get("uid")
        search= request.data.get("input")  #从前端接收的值
        if not search:
            return JsonResponse({'code': 999998, 'message': '输入不能为空'})
        obj = Image.objects.filter(uid_id=uid_id).filter(title_contains=search).order_by("id")
        if not obj:
            return JsonResponse({'code': 999999, 'message': '搜索结果为空'})
        serialize = ImageSerializer(obj, many=True)
        return JsonResponse(data={"data": serialize.data,
                                  }, code="999999", msg="搜索成功")