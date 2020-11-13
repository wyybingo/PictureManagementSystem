"""
实现思路：
（1）百度智能云注册：创建应用， 获取（ak和sk）    API Key和Secret Key   https://ai.baidu.com/ai-doc/REFERENCE/Ck3dwjgn3
（2）根据获取ak  和sk    获取access_token
（3）根据api调用https://ai.baidu.com/ai-doc/IMAGEPROCESS/Xk8a1ajdw

AppID
API Key
Secret Key
地标识别--毕业设计
22909559
OtbBHQlCdg48QIlI1cQLci0j
K8riLoUAmGKXof5CKILTe3K7lvZtnN5Z

"""
#

# encoding:utf-8
import requests
import requests
import base64
import os





def get_location(a):
    # 获取token
    ak = "OtbBHQlCdg48QIlI1cQLci0j"
    sk = "K8riLoUAmGKXof5CKILTe3K7lvZtnN5Z"
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + ak + '&client_secret=' + sk
    response = requests.get(host)
    access_token = response.json()["access_token"]
    print(access_token)
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/landmark"
    # 二进制方式打开图片文件
    # f = open(img, 'rb')
    a.seek(0)
    img = base64.b64encode(a.read())

    # img = base64.b64encode(img)

    params = {"image": img}
    print("图片参数为：",img)
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    print("地标tag为：",response.json()["result"]["landmark"])


    if len(response.json()["result"]["landmark"])==0:
        return  "其他"
    else:
        return response.json()["result"]["landmark"]
# img="/Users/wangyuanyuan/Documents/wyy/01_code/PicturesManagementSystem/pictures/test_img/故宫.jpeg"
# # # img="/Users/wangyuanyuan/Documents/wyy/01_code/PicturesManagementSystem/pictures/test_img/000159.jpg"
# a=get_location(img)
# print(a)




