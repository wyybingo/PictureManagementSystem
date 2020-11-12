"""
实现思路：
（1）百度智能云注册：创建应用， 获取（ak和sk）    API Key和Secret Keyhttps://ai.baidu.com/ai-doc/REFERENCE/Ck3dwjgn3
（2）根据获取ak  和sk    获取access_token
（3）根据api调用https://ai.baidu.com/ai-doc/IMAGEPROCESS/Xk8a1ajdw

"""
#

# encoding:utf-8
import requests
import requests
import base64
import os





def change_style(image_url,style_type):
    # 获取token
    ak = "f4wh1Tfy5hZSBC7dMzdrrgbR"
    sk = "QsTtHydILjTecNCjyzvSpmzfVsaUMOF5"
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + ak + '&client_secret=' + sk
    response = requests.get(host)
    access_token = response.json()["access_token"]
    request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/style_trans"

    # 二进制方式打开图片文件
    access_token = '24.109a3b4c2e77e23363cc0f0c2ea6e323.2592000.1603629121.282335-22758322'
    f = open(image_url, 'rb')
    img = base64.b64encode(f.read())
    # （3）根据access_token使用接口进行处理


    # 图像特效
    # 1.黑白图像上色
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    if style_type==1:
        params = {"image": img}
        request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/colourize"

    # 2.图像风格转换
    elif style_type==2:
        params = {"image": img, "option": "cartoon"}
        request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/style_trans"

    #3.人像动漫化
    elif style_type==3:
        params = {"image": img}
        request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/selfie_anime"

    #4.天空分割
    elif style_type==4:
        params = {"image": img}
        request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/sky_seg"

    # 5.图像去雾
    elif style_type == 5:
        params = {"image": img}
        request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/dehaze"

    # 6.图像对比度增强
    elif style_type == 6:
        params = {"image": img}
        request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/contrast_enhance"

    # 7.图像无损放大
    elif style_type == 7:
        params = {"image": img}
        request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/image_quality_enhance"

    # 8.拉伸图片恢复
    elif style_type == 8:
        params = {"image": img}
        request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/stretch_restore"

    # 9.图像修复
    elif style_type == 9:
        params = {"rectangle":[{'width': 92, 'top': 25, 'height': 36, 'left': 543}],"image":img}
        request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/sky_seg"

    # 10.图像清晰度增强
    elif style_type == 10:
        params = {"image": img}
        request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/image_definition_enhance"

    # 11.图像色彩增强
    elif style_type == 11:
        params = {"image": img}
        request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/color_enhance"
    else:
        pass
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(request_url, data=params, headers=headers)
    # 获取风格后的图片的64编码
    base64_img = response.json()
    if  "image" in base64_img:
        img_data = base64.b64decode(base64_img["image"])
        # 重新命名时间戳为新的图片名称
        import os, time
        pic_url = '/Users/wangyuanyuan/Documents/wyy/01_code/PicturesManagementSystem/uploads'
        t = int(time.time())
        save_path = os.path.join(pic_url, str(t) + ".jpg")
        with open(save_path, 'wb') as f:
            f.write(img_data)
            print('successful')
    else:
        print(base64_img["error_msg"])

pic_url="/Users/wangyuanyuan/Documents/wyy/01_code/PicturesManagementSystem/uploads/UNADJUSTEDNONRAW_thumb_1676.jpg"
change_style(pic_url,3)






#
# # 注意：如果是"data:image/jpg:base64,"，那你保存的就要以png格式，如果是"data:image/png:base64,"那你保存的时候就以jpg格式。

