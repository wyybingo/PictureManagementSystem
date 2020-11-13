from django.shortcuts import render
from rest_framework.views import APIView
from common_api.api.api_response import JsonResponse
from .models import Image,Auto_Tag,Location_Tag
import os
from pictures.serializers import ImageSerializer
from . import get_auto_tag,get_location_tag,get_image_info
import cv2
import base64
import imutils
import numpy as np




# Create your views here.

class upload_img(APIView):

    cur_path = os.path.dirname(os.path.realpath(__file__))



    def post(self, request):
        uid_id=request.POST.get("uid")
        img_files = request.FILES.getlist("file")
        repeat_img = []
        for img in img_files:
            # upload_dir = os.path.join(self.cur_path, "uploads")
            # file_path = os.path.join(upload_dir, img.name)
            # a=[img.file, img.field_name, img.name, img.content_type,
            #       img.size, img.charset, img.content_type_extra]
            # print(a)
            # 直接获取图片的类型，大小，名称
            img_type= img.content_type
            img_size=img.size
            img_name=img.name
            print("可以直接获取的图片基本信息为：", img_name,img_type,img_size)


            # 1.获取宽度，高度，拍摄时间
            img_width, img_height, img_time = get_image_info.get_picture_info(img)
            print("方法1获取图片基本信息为：",  img_width, img_height,  img_time)
            # print(img)
            # img.ContentLength,img.ContentType,img.FileName,img.InputStream
            # ,img.SaveAs("/Users/wangyuanyuan/Documents/wyy/01_code/PictureManagementSystem/PicturesManagementSystem/pictures"))


            # 2.获取图片自动分类,可以直接获取id
            auto_tag_id = get_auto_tag.detection(img)
            print("图片自动分类为：", auto_tag_id)

            # 3. 获取图片地标分类，只能获取地标文字
            location_tag = get_location_tag.get_location(img)
            print("地标分类为：", location_tag)
            location_id = Location_Tag.objects.filter(location_tag_name=location_tag)
            print("地标分类ID为：", location_id)

            # 如果地标存在，则直接获取地标id
            if location_id.exists():
                location_tag_id = location_id
            # 如果地标不存在，则直接获取地标id
            else:
                loc = Location_Tag(tag_name=img)
                loc.save()
                location_id = Location_Tag.objects.filter(tag_name=location_tag)
                location_tag_id = location_id

            upload_dir = os.path.join(self.cur_path, "uploads")
            file_path = os.path.join(upload_dir, img.name)
            pic_name = os.path.basename(file_path)
            images = Image(original=img, uid_id=uid_id, created=img_time, type=img_type, width=img_width,
                           height=img_height, size=img_size,auto_tag=auto_tag_id, location_tag=location_tag_id,title = pic_name)
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


        1.获取图片基本信息，保存到数据库
        2.获取图片地标tag
        (1) 先从表里根据tag名称查询是否有对应id,有的话就取对应id
        （2）如果没有的话就先落到对应分类表里，然后获取ID,
        """
        uid_id=request.GET.get("uid")
        obj = Image.objects.filter(uid_id=uid_id).order_by("id").values()
        # print("debug1:",obj)

        # lsobj = list(obj)
        # print(lsobj[0])
        # print('debug',obj['origin'])

        print(type(obj))

        for img in obj:
            # print('debug2:',img)
            print(type(img))

            pic_url = "/Users/wangyuanyuan/Documents/wyy/01_code/PicturesManagementSystem/" + img["original"]
            # print(pic_url)
            import base64
            with open(pic_url, 'rb') as f:
                base64_data = base64.b64encode(f.read())
                img["original"]=base64_data.decode()
                # print('ddp:', img['original'][:10])

                # print(img["original"])
        # for  imgs in obj :
        data=list(obj)
        # print("debug2：转为base64的obj:",data)
        # serialize = ImageSerializer(obj, many=True)  好用的
        # print("debug5:",serialize['original'])
        # print("debug3:",serialize.__dict__)
        # print(dict(serialize))
        # print("debug4:",serialize.keys())
        # print("debug5:",serialize)

        # return JsonResponse(data={"data": serialize.data,
        #                           }, code="999999", msg="搜索成功")  好用的
        return JsonResponse(data={"data": data,
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

